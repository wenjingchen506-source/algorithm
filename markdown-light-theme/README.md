# Markdown 浅色代码块模板

为 VuePress 1 默认主题 / Prism 的代码块结构编写：浅灰背景、独立行号栏、语言标签、彩色语法高亮和横向滚动。参考代码随想录的代码块结构，配色为重新设计。

## 查看效果

用浏览器打开同目录的 `preview.html`，不需要联网或安装依赖。预览中的高亮标签是静态示例；实际网站由 VuePress / Prism 生成。

## 用在 VuePress 1 中

1. 把 `code-light.css` 的**全部内容**复制到 Markdown 文档目录下的 `.vuepress/styles/index.styl`；已有内容时追加到末尾。这一步不需要 CSS 的 `@import`。
2. 在已有的 `.vuepress/config.js` 中合并下面的设置，保留其他配置：

   ```js
   module.exports = {
     markdown: {
       lineNumbers: true
     }
   }
   ```

3. 在 Markdown 中用三个反引号标注语言。`example.md` 可直接作为文章模板。

   ````markdown
   ## 我的代码

   ```cpp
   // 在这里写 C++ 代码
   int answer = 42;
   ```
   ````

指定行高亮可以写成 `cpp{3-5}`。字体大小、背景色等集中在 CSS 顶部的变量中。

VuePress 1 官方说明：[自定义样式](https://v1.vuepress.vuejs.org/config/#index-styl)、[行号配置](https://v1.vuepress.vuejs.org/config/#markdown-linenumbers)。

## 其他 Markdown 网页

这份 CSS 适配 `.theme-default-content` 内的 VuePress 1 / Prism HTML 结构，不是所有 Markdown 工具的通用皮肤。普通网页可以参考 `preview.html` 的结构，并在原有样式后加载 `code-light.css`；动态代码需要由 Prism 等工具生成 `.token` 高亮标签。行号也需要渲染器生成对应结构。

VitePress、MkDocs Material 和 highlight.js 的结构不同，需要调整选择器；单独复制 `.md` 文件不会携带配色。当前模板不包含复制按钮。
