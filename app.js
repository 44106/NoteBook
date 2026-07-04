const resources = Array.isArray(window.SITE_RESOURCES) ? window.SITE_RESOURCES : [];

const state = {
  query: "",
  semester: "全部",
  type: "全部",
  sort: "course",
};

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

function groupByCourse(items) {
  return items.reduce((acc, item) => {
    const key = `${item.semester} / ${item.course}`;
    if (!acc.has(key)) acc.set(key, []);
    acc.get(key).push(item);
    return acc;
  }, new Map());
}

function renderResources(items) {
  els.grid.innerHTML = "";
  els.empty.hidden = items.length > 0;
  els.title.textContent = state.query ? `搜索结果：${items.length} 个文件` : `全部资料：${items.length} 个文件`;

  const groups = groupByCourse(sortItems(items));
  groups.forEach((groupItems, courseName) => {
    const card = document.createElement("article");
    card.className = "course-card";

    const list = groupItems.map((item) => `
      <a class="resource" href="${encodePath(item.path)}" target="_blank" rel="noopener">
        <span>
          <span class="resource-title">${item.title}</span>
          <span class="resource-meta">
            <span>${item.fileName}</span>
            <span>${formatBytes(item.size)}</span>
            <span>${item.modified}</span>
          </span>
        </span>
        <span class="badge">${item.type}</span>
      </a>
    `).join("");

    card.innerHTML = `
      <header>
        <div>
          <h3>${courseName}</h3>
          <p>${groupItems.length} 个文件</p>
        </div>
      </header>
      <div class="resource-list">${list}</div>
    `;
    els.grid.appendChild(card);
  });
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

function init() {
  const courses = new Set(resources.map((item) => `${item.semester}/${item.course}`));
  els.totalCount.textContent = resources.length;
  els.courseCount.textContent = courses.size;

  els.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    render();
  });

  els.sort.addEventListener("change", (event) => {
    state.sort = event.target.value;
    render();
  });

  render();
}

init();
