# Python 竞赛笔记

按主题查阅，点进小节可以对照不同写法、样例、纠错过程和原始行号。

本地用浏览器打开 [浅色代码阅读页](index.html)。GitHub 仓库内可直接阅读下面的 Markdown。

- [Python 基础与常用 API](python.md) · 字符串、列表与映射、字典与频次统计、表达式与可迭代对象、字符串赋值与循环
- [竞赛输入输出与文件](io.md) · 竞赛快读与输出、本地文件与标准流切换、文件题的读写方式
- [数据结构与计数](structure.md) · 多数元素与摩尔投票、哈希集合与连续序列、从双倍数组还原
- [贪心与堆](greedy.md) · 排序与插入、区间任务调度、分段计算训练成本、堆相关练习题号、反悔贪心与堆、利润与类别数的权衡、工资比例与最大堆、双指针配对
- [前缀和与差分](difference.md) · 区间覆盖与前缀和、二分定位与差分计数
- [二分与答案边界](binary.md) · 冶炼金属的可行区间、二分答案分糖果
- [递推与组合计数](recurrence.md) · 跳台阶
- [DFS、枚举与回溯](dfs.md) · 递归深度与缓存、装箱与最少工作时段、逐位搜索最大数、记录方案与恢复现场、组合枚举、组合总和、子集枚举、排列枚举、选数与素数和、烤鸡的定长枚举、火星人与字典序后继、火柴加法、配料的酸度与苦度
- [BFS 与最短步数](bfs.md) · 网格上的多源 BFS、开关谜题的状态空间 BFS
- [图的表示与遍历](graph.md) · 沿后继搜索环、带权无向图与 DFS
- [位运算与子集](bits.md) · 用整数表示集合、按位枚举配料子集
- [数论与素数筛](math.md) · 筛法与区间计数、素数判定与分解

## 原始文件

- [Tsingpigdadademoban.py](originals/Tsingpigdadademoban.py) · 1,050 行
- [dfs.py](originals/dfs.py) · 771 行
- [reshensaibaiduzhixing.py](originals/reshensaibaiduzhixing.py) · 46 行
- [rthsrth.py](originals/rthsrth.py) · 6 行

原件保留原始字节，包括缩进、换行和空行。笔记中标为草稿的片段保留原写法。

知识点编排参考[开放 CS/AI 知识库的 Python 代码模板](https://wiki.dwj601.cn/ds-and-algo/templates-py/)。代码块使用本仓库的[浅色主题](../../markdown-light-theme/code-light.css)。

补充材料时，将原件放入 originals，在 catalog.tsv 中按原始行号标记每段的起始行及所属知识点，然后运行 `python notes/python/build.py` 更新阅读页。
