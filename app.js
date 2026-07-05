let resources = Array.isArray(window.SITE_RESOURCES) ? window.SITE_RESOURCES : [];

const REPO_OWNER = "44106";
const REPO_NAME = "NoteBook";
const REPO_BRANCH = "main";
const API_TREE_URL = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/git/trees/${REPO_BRANCH}?recursive=1`;
const RAW_FILE_BASE_URL = `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${REPO_BRANCH}`;
const IGNORED_INDEX_PATHS = new Set([".gitignore", ".nojekyll", "index.html", "app.js", "styles.css", "site-data.js"]);

const state = {
  query: "",
  semester: "全部",
  type: "全部",
  sort: "course",
  source: "静态索引",
};

const openFolders = new Set();

const els = {
  totalCount: document.querySelector("#total-count"),
  courseCount: document.querySelector("#course-count"),
  search: document.querySelector("#search-input"),
  semesterFilters: document.querySelector("#semester-filters"),
  typeFilters: document.querySelector("#type-filters"),
  sort: document.querySelector("#sort-select"),
  title: document.querySelector("#result-title"),
  grid: document.querySelector("#course-grid"),
  empty: document.querySelector("#empty-state"),
};

let markdownViewer = null;

function getFileType(fileName) {
  const dotIndex = fileName.lastIndexOf(".");
  if (dotIndex <= 0 || dotIndex === fileName.length - 1) return "file";
  return fileName.slice(dotIndex + 1).toLowerCase();
}

function getTitle(fileName) {
  const dotIndex = fileName.lastIndexOf(".");
  return dotIndex > 0 ? fileName.slice(0, dotIndex) : fileName;
}

function getPathParts(path) {
  return String(path || "").split("/").filter(Boolean);
}

function isIndexablePath(path) {
  if (!path || IGNORED_INDEX_PATHS.has(path)) return false;
  return !path.startsWith(".git/") && !path.startsWith(".agents/") && !path.startsWith(".codex/");
}

function resourceFromTreeItem(item) {
  const parts = getPathParts(item.path);
  const fileName = parts[parts.length - 1] || item.path;
  return {
    title: getTitle(fileName),
    fileName,
    path: item.path,
    semester: parts[0] || "根目录",
    course: parts[1] || "未分类",
    type: getFileType(fileName),
    size: item.size || 0,
    modified: "仓库最新",
  };
}

async function loadDynamicResources() {
  const response = await fetch(`${API_TREE_URL}&t=${Date.now()}`, {
    headers: { Accept: "application/vnd.github+json" },
    cache: "no-store",
  });
  if (!response.ok) {
    throw new Error(`GitHub API ${response.status}`);
  }

  const data = await response.json();
  if (!Array.isArray(data.tree)) {
    throw new Error("GitHub API response missing tree");
  }

  return data.tree
    .filter((item) => item.type === "blob" && isIndexablePath(item.path))
    .map(resourceFromTreeItem);
}

function formatBytes(bytes) {
  if (!Number.isFinite(bytes) || bytes <= 0) return "0 KB";
  const units = ["B", "KB", "MB", "GB"];
  let value = bytes;
  let index = 0;
  while (value >= 1024 && index < units.length - 1) {
    value /= 1024;
    index += 1;
  }
  return `${value.toFixed(index === 0 ? 0 : 1)} ${units[index]}`;
}

function encodePath(path) {
  return String(path)
    .split("/")
    .map((part) => encodeURIComponent(part))
    .join("/");
}

function getRawFileUrl(path) {
  return `${RAW_FILE_BASE_URL}/${encodePath(path)}`;
}

async function downloadFile(item) {
  const response = await fetch(getRawFileUrl(item.path));
  if (!response.ok) {
    throw new Error(`Download failed: ${response.status}`);
  }

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = item.displayName || item.fileName || "download";
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function ensureMarkdownViewer() {
  if (markdownViewer) return markdownViewer;

  const overlay = document.createElement("div");
  overlay.className = "markdown-viewer";
  overlay.hidden = true;
  overlay.innerHTML = `
    <div class="markdown-dialog" role="dialog" aria-modal="true" aria-labelledby="markdown-title">
      <header class="markdown-header">
        <div>
          <p class="eyebrow">Markdown</p>
          <h2 id="markdown-title"></h2>
        </div>
        <div class="markdown-actions">
          <a class="markdown-raw-link" target="_blank" rel="noopener">原文</a>
          <button class="markdown-close" type="button" aria-label="关闭">关闭</button>
        </div>
      </header>
      <article class="markdown-body"></article>
    </div>
  `;

  const close = () => {
    overlay.hidden = true;
    document.body.classList.remove("viewer-open");
  };

  overlay.querySelector(".markdown-close").addEventListener("click", close);
  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) close();
  });
  document.addEventListener("keydown", (event) => {
    if (!overlay.hidden && event.key === "Escape") close();
  });

  document.body.appendChild(overlay);
  markdownViewer = {
    overlay,
    title: overlay.querySelector("#markdown-title"),
    rawLink: overlay.querySelector(".markdown-raw-link"),
    body: overlay.querySelector(".markdown-body"),
  };
  return markdownViewer;
}

function renderMarkdown(markdown) {
  if (!window.marked || !window.DOMPurify) {
    const escaped = markdown
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    return `<pre>${escaped}</pre>`;
  }

  window.marked.setOptions({
    breaks: true,
    gfm: true,
  });
  return window.DOMPurify.sanitize(window.marked.parse(markdown));
}

async function openMarkdownViewer(item) {
  const viewer = ensureMarkdownViewer();
  const rawUrl = getRawFileUrl(item.path);
  viewer.title.textContent = item.displayName || item.fileName || item.title || "Markdown";
  viewer.rawLink.href = rawUrl;
  viewer.body.innerHTML = `<p class="markdown-loading">正在加载...</p>`;
  viewer.overlay.hidden = false;
  document.body.classList.add("viewer-open");

  try {
    const response = await fetch(rawUrl);
    if (!response.ok) {
      throw new Error(`Markdown fetch failed: ${response.status}`);
    }
    const markdown = await response.text();
    viewer.body.innerHTML = renderMarkdown(markdown);
  } catch (error) {
    console.warn("Markdown render failed:", error);
    viewer.body.innerHTML = `
      <p class="markdown-error">Markdown 加载失败。</p>
      <p><a href="${rawUrl}" target="_blank" rel="noopener">打开原文</a></p>
    `;
  }
}

function countBy(key) {
  return resources.reduce((acc, item) => {
    const value = item[key] || "未分类";
    acc.set(value, (acc.get(value) || 0) + 1);
    return acc;
  }, new Map());
}

function makeFilter(container, values, activeValue, onClick) {
  container.innerHTML = "";
  values.forEach(([label, count]) => {
    const button = document.createElement("button");
    button.className = `filter-btn${label === activeValue ? " active" : ""}`;
    button.type = "button";
    button.innerHTML = `<span>${label}</span><small>${count}</small>`;
    button.addEventListener("click", () => onClick(label));
    container.appendChild(button);
  });
}

function getFiltered() {
  const query = state.query.trim().toLowerCase();
  return resources.filter((item) => {
    const matchesSemester = state.semester === "全部" || item.semester === state.semester;
    const matchesType = state.type === "全部" || item.type === state.type;
    const haystack = `${item.title} ${item.fileName} ${item.course} ${item.semester} ${item.type}`.toLowerCase();
    return matchesSemester && matchesType && (!query || haystack.includes(query));
  });
}

function sortItems(items) {
  const sorted = [...items];
  const byText = (a, b, key) => String(a[key] || "").localeCompare(String(b[key] || ""), "zh-CN");
  if (state.sort === "modified") {
    sorted.sort((a, b) => String(b.modified).localeCompare(String(a.modified)) || byText(a, b, "course"));
  } else if (state.sort === "type") {
    sorted.sort((a, b) => byText(a, b, "type") || byText(a, b, "course"));
  } else if (state.sort === "size") {
    sorted.sort((a, b) => (b.size || 0) - (a.size || 0));
  } else {
    sorted.sort((a, b) => byText(a, b, "semester") || byText(a, b, "course") || byText(a, b, "title"));
  }
  return sorted;
}

function createFolderNode(name = "root") {
  return {
    name,
    folders: new Map(),
    files: [],
    count: 0,
  };
}

function createTree(items) {
  const root = createFolderNode();
  items.forEach((item) => {
    const parts = String(item.path || item.fileName || item.title).split("/").filter(Boolean);
    const fileName = parts.pop() || item.fileName || item.title;
    let node = root;
    node.count += 1;

    parts.forEach((part) => {
      if (!node.folders.has(part)) node.folders.set(part, createFolderNode(part));
      node = node.folders.get(part);
      node.count += 1;
    });

    node.files.push({ ...item, displayName: fileName });
  });
  return root;
}

function getFolderKey(parentKey, name) {
  return parentKey ? `${parentKey}/${name}` : name;
}

function shouldOpenFolder(key, depth) {
  if (state.query.trim()) return true;
  return openFolders.has(key);
}

function renderTreeNode(node, container, depth = 0, parentKey = "") {
  const folders = [...node.folders.values()].sort((a, b) => a.name.localeCompare(b.name, "zh-CN"));
  const files = sortItems(node.files);

  folders.forEach((folder) => {
    const folderKey = getFolderKey(parentKey, folder.name);
    const details = document.createElement("details");
    details.className = "tree-folder";
    details.open = shouldOpenFolder(folderKey, depth);
    details.dataset.key = folderKey;

    const summary = document.createElement("summary");
    summary.className = "tree-folder-summary";
    summary.innerHTML = `
      <span class="tree-folder-name">${folder.name}</span>
      <span class="tree-count">${folder.count}</span>
    `;
    details.appendChild(summary);

    const children = document.createElement("div");
    children.className = "tree-children";
    renderTreeNode(folder, children, depth + 1, folderKey);
    details.appendChild(children);

    details.addEventListener("toggle", () => {
      if (details.open) {
        openFolders.add(folderKey);
      } else {
        openFolders.delete(folderKey);
      }
    });

    container.appendChild(details);
  });

  files.forEach((item) => {
    const link = document.createElement("a");
    link.className = "tree-file";
    const isPng = item.type === "png";
    const isMarkdown = item.type === "md";
    link.href = isPng || isMarkdown ? getRawFileUrl(item.path) : encodePath(item.path);
    if (isPng) {
      link.download = item.displayName || item.fileName || "";
      link.addEventListener("click", async (event) => {
        event.preventDefault();
        try {
          await downloadFile(item);
        } catch (error) {
          console.warn("PNG download failed, falling back to raw file URL:", error);
          window.location.href = getRawFileUrl(item.path);
        }
      });
    } else if (isMarkdown) {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        openMarkdownViewer(item);
      });
    } else {
      link.target = "_blank";
      link.rel = "noopener";
    }
    link.innerHTML = `
      <span class="tree-file-main">
        <span class="tree-file-name">${item.displayName}</span>
        <span class="resource-meta">
          <span>${formatBytes(item.size)}</span>
          <span>${item.modified}</span>
        </span>
      </span>
      <span class="badge">${item.type}</span>
    `;
    container.appendChild(link);
  });
}

function renderResources(items) {
  els.grid.innerHTML = "";
  els.empty.hidden = items.length > 0;
  els.title.textContent = state.query
    ? `搜索结果：${items.length} 个文件`
    : `全部资料：${items.length} 个文件 · ${state.source}`;

  if (items.length === 0) return;

  const tree = document.createElement("div");
  tree.className = "file-tree";
  renderTreeNode(createTree(sortItems(items)), tree);
  els.grid.appendChild(tree);
}

function renderFilters() {
  const semesterCounts = [["全部", resources.length], ...[...countBy("semester").entries()].sort()];
  const typeCounts = [["全部", resources.length], ...[...countBy("type").entries()].sort((a, b) => b[1] - a[1])];

  makeFilter(els.semesterFilters, semesterCounts, state.semester, (value) => {
    state.semester = value;
    render();
  });

  makeFilter(els.typeFilters, typeCounts, state.type, (value) => {
    state.type = value;
    render();
  });
}

function render() {
  renderFilters();
  renderResources(getFiltered());
}

function setStats() {
  const courses = new Set(resources.map((item) => `${item.semester}/${item.course}`));
  els.totalCount.textContent = resources.length;
  els.courseCount.textContent = courses.size;
}

async function init() {
  setStats();

  els.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    render();
  });

  els.sort.addEventListener("change", (event) => {
    state.sort = event.target.value;
    render();
  });

  render();

  try {
    const dynamicResources = await loadDynamicResources();
    if (dynamicResources.length > 0) {
      resources = dynamicResources;
      state.source = "仓库实时索引";
      setStats();
      render();
    }
  } catch (error) {
    state.source = "静态索引";
    console.warn("Using static site-data.js index:", error);
    render();
  }
}

init();
