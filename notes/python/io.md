# 竞赛输入输出与文件

[主题目录](README.md) · [浅色阅读页](index.html#io)

先看标准输入的入口，再对照读文件、重定向和逐行解析的写法。

- [竞赛快读与输出](#note-tsingpigdadademoban-1)
- [本地文件与标准流切换](#note-tsingpigdadademoban-882)
- [文件题的读写方式](#note-tsingpigdadademoban-920)

<a name="note-tsingpigdadademoban-1"></a>

## 竞赛快读与输出

读入整数的入口

原稿 [Tsingpigdadademoban.py · L1–6](originals/Tsingpigdadademoban.py#L1-L6)

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
if __name__=='__main__':
    solve()
```

依次读取网格元素与批量输出

原稿 [Tsingpigdadademoban.py · L33–36](originals/Tsingpigdadademoban.py#L33-L36)

```python
grid=[int(next(da)) for _ in range(m) for _ in range(n)]

sys.stdout.write('\n'.join(out)+'\n')

```

逐行读取与 strip 的两次练习

原稿 [Tsingpigdadademoban.py · L43–49](originals/Tsingpigdadademoban.py#L43-L49)

```python
import sys
for line in sys.stdin:
    line=line.strip()

for line in sys.stdin:
    line=line.strip()

```

DFS 练习文件中的输入骨架

原稿 [dfs.py · L1–8](originals/dfs.py#L1-L8)

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
if __name__=='__main__':
    solve()



```


<a name="note-tsingpigdadademoban-882"></a>

## 本地文件与标准流切换

检测 in.txt 后重定向输入、输出

原稿 [Tsingpigdadademoban.py · L882–907](originals/Tsingpigdadademoban.py#L882-L907)

```python
import sys
import os
def solve():
    # 这里的逻辑一行都不用改！
    da = iter(sys.stdin.read().split())
    try:
        n = int(next(da))
        # ... 你的其他算法逻辑 ...
        
        # 测试输出
        sys.stdout.write(f"成功读取了数字: {n}\n")
        
    except StopIteration:
        return
if __name__ == '__main__':
    # ---------------- 核心文件读写模板 ----------------
    # 极度严谨的“自动环境切换”逻辑：
    # 判断当前目录下是否存在名为 'in.txt' 的文件
    if os.path.exists('in.txt'):
        # 1. 劫持标准输入：让 sys.stdin 从控制台输入变成读取 in.txt
        sys.stdin = open('in.txt', 'r', encoding='utf-8')
        # 2. 劫持标准输出：让所有的 print 和 sys.stdout.write 统统写入 out.txt
        sys.stdout = open('out.txt', 'w', encoding='utf-8')
    # --------------------------------------------------   
    solve()

```

精简写法与文件名字符串的提醒

原稿 [Tsingpigdadademoban.py · L908–919](originals/Tsingpigdadademoban.py#L908-L919)

```python
import sys
import os
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    sys.stdout.write('\n')
if __name__ =='__main__':
    if os.path.exists('in.txt'):
        sys.stdin=open('in.txt','r',encoding='utf-8')#是字符串！！！
        sys.stdout=open('out.txt','w',encoding='utf-8')
    solve()
        
```


<a name="note-tsingpigdadademoban-920"></a>

## 文件题的读写方式

用 with 同时管理输入输出，保留两种写答案的方法

原稿 [Tsingpigdadademoban.py · L920–953](originals/Tsingpigdadademoban.py#L920-L953)

```python
def solve():
    # 1. 极其优雅的“双管齐下”写法
    # 用 with open 同时打开两个文件，保证程序结束或报错时，文件会自动安全关闭！
    with open('in.txt', 'r', encoding='utf-8') as fin, \
         open('out.txt', 'w', encoding='utf-8') as fout:
        
        # 2. 继承我们的“快读”衣钵
        # 把 fin (文件对象) 里的内容瞬间全部吸干，切分并做成迭代器
        da = iter(fin.read().split())
        
        try:
            # 假设题目第一行给了两个数 n 和 m
            n = int(next(da))
            m = int(next(da))
            
            # --- 在这里写你的核心算法 ---
            # 假设答案是 n 和 m 的和
            ans = n + m
            
            # 3. 写入答案 (两种标准写法任选其一)
            
            # 写法 A：用原生的 write（记得手动加换行符 \n）
            fout.write(str(ans) + '\n')
            
            # 写法 B：极其推荐！借用 print 的力量，把输出重定向到 fout
            # 这种写法不用你自己转 str，也不用手动加 \n，非常舒服
            # print(ans, file=fout)
            
        except StopIteration:
            pass

if __name__ == '__main__':
    solve()

```

从文件读入并在终端输出

原稿 [Tsingpigdadademoban.py · L954–972](originals/Tsingpigdadademoban.py#L954-L972)

```python
# 模式一：读取文件，处理数据，最后print输出
def solve():
    # 比赛中：如果是国赛文件题，直接读题目给的文件名
    # 本地刷题时：用你的模板保证 in.txt 存在即可
    filename = 'primes.txt' 
    
    with open(filename, 'r', encoding='utf-8') as f:
        # 建议根据数据量选择读取方式
        # 方式A（小数据）：content = f.readlines()
        # 方式B（大数据）：iter(f.read().split())
        data = iter(f.read().split())
        
        # 你的逻辑...
        print(ans)

if __name__ == '__main__':
    solve()


```

逐行处理并写到 out.txt

原稿 [Tsingpigdadademoban.py · L973–986](originals/Tsingpigdadademoban.py#L973-L986)

```python
# 模式二：读取 in.txt，处理后写入 out.txt
def solve():
    with open('log.txt', 'r', encoding='utf-8') as fin, \
         open('result.txt', 'w', encoding='utf-8') as fout:
        
        # 将处理逻辑直接关联到 fout
        for line in fin:
            # 你的处理逻辑
            processed_data = line.strip() 
            fout.write(processed_data + '\n')

if __name__ == '__main__':
    solve()

```

按逗号拆字段，末尾保留未完成的 with 语句

原稿 [Tsingpigdadademoban.py · L987–1001](originals/Tsingpigdadademoban.py#L987-L1001)

```python
# 模式三：结构化解析
import re

def solve():
    with open('bill.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # 常见技巧：split() 空格，或者用 re.split() 切割复杂字符串
            parts = line.strip().split(',')
            # 处理 parts...


with open('in.txt','r',encoding='utf-8') as fin,\
     open('out.txt','w',encoding='utf-8') as fout


```
