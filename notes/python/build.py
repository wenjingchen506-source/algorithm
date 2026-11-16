"""从原稿与 catalog.tsv 生成分主题的 Markdown 及离线阅读页。Python 3.8+。"""
import builtins
import csv
import io
import keyword
import tokenize
from collections import defaultdict
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFERENCE = 'https://wiki.dwj601.cn/ds-and-algo/templates-py/'
TOPICS = {
    'python': ('Python 基础与常用 API', '从字符串查找、字典计数到表达式，按操作查找原来的小实验。'),
    'io': ('竞赛输入输出与文件', '先看标准输入的入口，再对照读文件、重定向和逐行解析的写法。'),
    'structure': ('数据结构与计数', '用集合删去已处理的元素，用频次表记录配对次数，或用抵消计数维护候选值。'),
    'greedy': ('贪心与堆', '先确定处理顺序，再判断要保留哪项选择。反悔型题目用堆取出最值得撤回的一项。'),
    'difference': ('前缀和与差分', '把一次区间更新记录在两个端点上，再通过前缀和恢复每个位置的覆盖次数。'),
    'binary': ('二分与答案边界', '先写出候选值的可行条件，再判断要找第一个可行值还是最后一个可行值。'),
    'recurrence': ('递推与组合计数', '同一道跳台阶题，从递归、滚动变量、特征方程和组合计数四个角度看。'),
    'dfs': ('DFS、枚举与回溯', '从选或不选、排列和组合开始，再看怎样记录路径、限制下一层起点，以及何时恢复访问标记。'),
    'bfs': ('BFS 与最短步数', '网格扩散与开关谜题共用按层扩展的写法，队列分别存坐标和灯光状态。'),
    'graph': ('图的表示与遍历', '对照矩阵和邻接表存边的方式，再看沿后继搜索时如何记录访问深度。'),
    'bits': ('位运算与子集', '让每一位表示是否选中一个元素，用掩码查询、修改或枚举整个集合。'),
    'math': ('数论与素数筛', '从单次试除到批量筛选，再用前缀和做区间查询、用最小质因子表做分解。'),
}
RELATED = {
    '选数与素数和': ('math', '素数判定与分解'),
    '素数判定与分解': ('dfs', '选数与素数和'),
    '配料的酸度与苦度': ('bits', '按位枚举配料子集'),
    '按位枚举配料子集': ('dfs', '配料的酸度与苦度'),
    '开关谜题的状态空间 BFS': ('bits', '用整数表示集合'),
}


def read_catalog():
    groups = defaultdict(lambda: defaultdict(list))
    with (HERE / 'catalog.tsv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    sources = defaultdict(list)
    for row in rows:
        sources[row['source']].append(row)
    originals = HERE / 'originals'
    if set(sources) != {p.name for p in originals.glob('*.py')}:
        raise ValueError('原件与目录中的文件名不一致')
    counts = {}
    for name, entries in sources.items():
        lines = (originals / name).read_text(encoding='utf-8').splitlines(keepends=True)
        counts[name] = len(lines)
        starts = [int(r['start']) for r in entries] + [len(lines) + 1]
        if starts[0] != 1 or sorted(set(starts)) != starts:
            raise ValueError(f'{name} 的起始行需要从 1 开始，且严格递增')
        for row, start, stop in zip(entries, starts, starts[1:]):
            if row['topic'] not in TOPICS or row['format'] not in ('python', 'text'):
                raise ValueError(row)
            row.update(first=start, last=stop-1, body=''.join(lines[start-1:stop-1]))
            groups[row['topic']][row['concept']].append(row)
    return groups, counts


def highlight(source):
    # tokenize 只读文本；遇到未闭合的实验片段时，剩余部分按原文显示。
    offsets = [0]
    for line in source.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    classes = {tokenize.NUMBER: 'number', tokenize.STRING: 'string', tokenize.COMMENT: 'comment'}
    parts, cursor, prev = [], 0, ''
    try:
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            cls = classes.get(tok.type)
            if tok.type == tokenize.NAME:
                if keyword.iskeyword(tok.string):
                    cls = 'keyword'
                elif prev in ('def', 'class'):
                    cls = 'function' if prev == 'def' else 'class-name'
                elif tok.string in vars(builtins):
                    cls = 'builtin'
            prev = tok.string
            if cls:
                start = offsets[tok.start[0]-1] + tok.start[1]
                end = offsets[tok.end[0]-1] + tok.end[1]
                parts.extend((escape(source[cursor:start]), f'<span class="token {cls}">{escape(source[start:end])}</span>'))
                cursor = end
    except (tokenize.TokenError, SyntaxError):
        pass
    parts.append(escape(source[cursor:]))
    return ''.join(parts)


def html_excerpt(row):
    first, last, body = row['first'], row['last'], row['body']
    if row['format'] == 'text':
        return '<div class="original-prose">' + escape(body) + '</div>'
    numbers = '<br>'.join(map(str, range(first, last+1)))
    return (f'<div class="language-python line-numbers-mode"><pre tabindex="0"><code>{highlight(body)}</code></pre>'
            f'<div class="line-numbers-wrapper" aria-hidden="true">{numbers}</div></div>')


def write(name, content):
    (HERE / name).write_bytes(content.encode('utf-8'))


def main():
    groups, counts = read_catalog()
    anchors = {
        (topic, concept): f"note-{Path(rows[0]['source']).stem.lower()}-{rows[0]['first']}"
        for topic, concepts in groups.items() for concept, rows in concepts.items()
    }
    idx = ['# Python 竞赛笔记', '',
           '按主题查阅，点进小节可以对照不同写法、样例、纠错过程和原始行号。', '',
           '本地用浏览器打开 [浅色代码阅读页](index.html)。GitHub 仓库内可直接阅读下面的 Markdown。', '']
    nav, chapters = [], []
    for topic, (title, intro) in TOPICS.items():
        concepts = groups[topic]
        idx.append(f'- [{title}]({topic}.md) · ' + '、'.join(concepts))
        nav.append(f'<li><a href="#{topic}">{title}</a></li>')
        chapter = [f'<section id="{topic}"><h2>{title}</h2><p>{intro}</p>']
        md = [f'# {title}', '', f'[主题目录](README.md) · [浅色阅读页](index.html#{topic})', '', intro, '']
        links = []
        for concept in concepts:
            md.append(f'- [{concept}](#{anchors[topic, concept]})')
            links.append(f'<a href="#{topic}-{concept.replace(" ", "-")}">{concept}</a>')
        chapter.append('<div class="local-nav">' + ' · '.join(links) + '</div>')
        for concept, excerpts in concepts.items():
            anchor = f'{topic}-{concept.replace(" ", "-")}'
            md.extend(('', f'<a name="{anchors[topic, concept]}"></a>', '', f'## {concept}', ''))
            chapter.append(f'<h3 id="{anchor}">{concept}</h3>')
            if concept in RELATED:
                related_topic, related = RELATED[concept]
                md.extend((f'关联知识点 · [{related}]({related_topic}.md#{anchors[related_topic, related]})', ''))
                chapter.append(f'<p>关联知识点 · <a href="#{related_topic}-{related.replace(" ", "-")}">{related}</a></p>')
            for row in excerpts:
                name, first, last, body = row['source'], row['first'], row['last'], row['body']
                ref = f'{name} · L{first}–{last}'
                md.extend((row['reading'], '', f'原稿 [{ref}](originals/{name}#L{first}-L{last})', ''))
                if row['format'] == 'text':
                    md.append('\n'.join('> ' + line for line in body.splitlines()))
                else:
                    md.append('```python\n' + body + ('' if body.endswith('\n') else '\n') + '```')
                md.append('')
                chapter.append(f'<article data-file="{name}" data-first="{first}" data-last="{last}">'
                               f'<h4>{escape(row["reading"])}</h4>'
                               f'<a class="source" href="originals/{name}">{ref}</a>{html_excerpt(row)}</article>')
        write(topic + '.md', '\n'.join(md))
        chapters.extend(chapter + ['</section>'])
    idx.extend(('', '## 原始文件', ''))
    for name, count in counts.items():
        idx.append(f'- [{name}](originals/{name}) · {count:,} 行')
    idx.extend(('', '原件保留原始字节，包括缩进、换行和空行。笔记中标为草稿的片段保留原写法。', '',
                f'知识点编排参考[开放 CS/AI 知识库的 Python 代码模板]({REFERENCE})。代码块使用本仓库的[浅色主题](../../markdown-light-theme/code-light.css)。', '',
                '补充材料时，将原件放入 originals，在 catalog.tsv 中按原始行号标记每段的起始行及所属知识点，然后运行 `python notes/python/build.py` 更新阅读页。', ''))
    write('README.md', '\n'.join(idx))
    layout = (HERE / 'reader-template.html').read_text(encoding='utf-8')
    write('index.html', layout.replace('<!-- topics -->', '\n'.join(nav)).replace('<!-- chapters -->', '\n'.join(chapters)))
    print(f'{len(counts)} 个文件，{sum(counts.values())} 行，{len(groups)} 个主题，'
          f'{sum(map(len, groups.values()))} 个知识点')


if __name__ == '__main__':
    main()
