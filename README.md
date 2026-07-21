# 24能工智人资料库

这是 24 级智能工程与创意设计（智能）相关课程的共享资料库。仓库同时是资料的存放位置和静态网站的源码；网站会按照学期、课程和文件类型展示资料，并支持下载、预览 Markdown 和打包下载文件夹。

## 目录约定

网站只将以下两个目录中的文件视为知识库资料：

```text
大二春夏/
大二秋冬/
```

目录的前两级会显示为“学期 / 课程”。建议按下面的形式新增资料：

```text
大二春夏/
  课程名称，学分/
    复习资料.pdf
    历年卷/
      2025-2026.pdf
```

根目录的 `index.html`、`app.js`、`styles.css`、`site-data.js`、本 README 和 `scripts/` 是网站或维护文件，不会出现在网页资料列表中。不要把网页构建文件、临时文件或个人配置放进两个学期目录。

## 上传资料

1. 在对应学期下找到或新建课程目录，课程名建议包含学分，便于识别。
2. 将资料放入课程目录；可以按“课件”“历年卷”“随堂笔记”等创建子目录。
3. 检查文件名。使用清楚、可搜索的名称，避免上传重复文件、编辑器临时文件和无关的构建产物。
4. 刷新静态索引：

   ```powershell
   .\scripts\generate-site-data.ps1
   ```

5. 确认生成结果包含新增资料：

   ```powershell
   git status
   ```

6. 提交并推送资料和更新后的 `site-data.js`：

   ```powershell
   git add "大二春夏" site-data.js
   git commit -m "补充课程资料"
   git push origin main
   ```

   若资料在秋冬学期，将命令中的 `大二春夏` 换为 `大二秋冬`。也可以在 GitHub 网页上传文件，但仍需在本地运行索引脚本并提交新的 `site-data.js`，以保证离线或 API 不可用时网站资料完整。

## 更新网站

页面由以下文件组成：

| 文件 | 用途 |
| --- | --- |
| `index.html` | 页面结构与外部脚本引用 |
| `styles.css` | 页面样式 |
| `app.js` | 搜索、筛选、下载、Markdown 预览和实时索引逻辑 |
| `site-data.js` | 静态资料索引，由脚本生成，不建议手改 |

修改网页后，在浏览器打开 `index.html` 做基本检查；涉及资料范围或目录规则时，也要运行 `generate-site-data.ps1`。若调整了 `app.js` 或 `site-data.js`，请同步更新 `index.html` 中对应脚本 URL 的 `v=` 参数，避免访问者命中浏览器缓存。

本项目按 GitHub Pages 的静态站点结构组织。若仓库启用了 Pages，推送后会按仓库的 Pages 配置更新；在仓库的 **Settings -> Pages** 可以查看发布状态、发布分支和站点地址。

## 索引规则

- `site-data.js` 是静态索引，直接由当前工作区的两个学期目录生成。
- 网页加载后会尝试读取 GitHub 仓库树作为实时索引；实时索引也只接受 `大二春夏/` 和 `大二秋冬/` 下的文件。
- 实时请求失败时，网页自动回退到静态索引。因此每次新增、删除或重命名资料后都应提交更新后的 `site-data.js`。

## 提交前检查

```powershell
.\scripts\generate-site-data.ps1
node --check app.js
git diff --check
git status
```

请避免直接修改 `site-data.js`，也不要提交 `.agents/`、`.codex/`、编辑器缓存、编译中间文件或来源不明的敏感资料。
