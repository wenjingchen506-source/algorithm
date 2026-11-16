# Python 竞赛笔记

## 目录

- [Python 基础与常用 API](#topic-python)
- [竞赛输入输出与文件](#topic-io)
- [数据结构与计数](#topic-structure)
- [贪心与堆](#topic-greedy)
- [前缀和与差分](#topic-difference)
- [二分与答案边界](#topic-binary)
- [递推与组合计数](#topic-recurrence)
- [DFS、枚举与回溯](#topic-dfs)
- [BFS 与最短步数](#topic-bfs)
- [图的表示与遍历](#topic-graph)
- [位运算与子集](#topic-bits)
- [数论与素数筛](#topic-math)

<a name="topic-python"></a>

## Python 基础与常用 API

从字符串查找、字典计数到表达式，按操作查找原来的小实验。

- [字符串、列表与映射](#note-tsingpigdadademoban-7)
- [字典与频次统计](#note-tsingpigdadademoban-14)
- [表达式与可迭代对象](#note-tsingpigdadademoban-39)
- [字符串赋值与循环](#note-rthsrth-1)
- [函数参数与运算符映射](#knowledge-params)
- [月份与条件分支](#knowledge-season)
- [矩阵遍历与网格模拟](#knowledge-matrix)
- [字母表循环移位](#knowledge-rot)
- [列表插入、排序与索引](#knowledge-sort)

<a name="note-tsingpigdadademoban-7"></a>

### 字符串、列表与映射

首次出现的位置、矩阵展平与 find

```python
# 返回 string 指定范围中 str 首次出现的位置
list(map(s.index,s))  # 返回字符索引数组，返回的是第一次出现的索引！如 "abcba"-> [0,1,2,1,0]

c=[e for row in matrix for e in row]

s.find(obj)#找不到返回-1，不会报错
```

对两个序列逐项求和

```python
map(lambda x,y :x+y,[1,2],[3,4])
```

反向切片与起止位置

```python
#反向输出################################################################
a=input()
print(a[::-1])
#start:切片的起始位置（包含该位置）;步长为正:默认0；步长为负:默认 len (a)-1
#end:切片的结束位置（不包含该位）;步长为正:默认len(a)；步长为负:默认-len(a)-1
#等价于从头）
#step:切片的步长（每次移动的步数）；正数 = 正向遍历，负数 = 反向遍历;默认 1
```

去掉末尾的 0，再倒序输出

```python
##41一行数除去最后一0其余倒序输出
n=list(map(int ,input().split()))
n.pop()
n.reverse()
print(' '.join(map(str , n)))
```

循环拼接、join 与预分配列表

> 杀手三：+=拼接字符串；解药：列表拼接法

```python
s=''
for i in range(100000):
    s+=str(i)

res=[]
for i in range(100000):
    res.append(str(i))append虽然是O(1)但要自己找地然后搬家
s=''.join(res)
```

> 杀手四：当然这样也不好！解药：空间预分配

```python
res=[0]*100000
for i in range(100000):
    res[i]=i
```

把指定字符替换成星号

```python
print(input().replace('5','*'))
```

查找子串位置的速记

```python
s=input()
print(s.find(Bob))
```

取各单词的首字母并转大写

```python
n = list(input().split())
for i in range(len(n)):
    n[i][0]=char(ord(n[i][0])+97-65)
print(' '.join(n))

n=input().split()
ans=[w[0].upper() for w in n]
print(''.join(ans))
```

对指定闭区间做替换，对照初稿与切片拼接版本

> 错答

```python
n,m=map(int,input().split())
a=input()
for _ in range(m):
    s=list(input().split())
    s[0],s[1]=int(s[0]),int(s[1])
    a[s[0]:s[1]].replace(s[2],s[3])
print(a)

n, m = map(int, input().split())
a = input().strip()
for _ in range(m):
    # 读取一行操作指令
    data = input().split()
    l, r = int(data[0]), int(data[1])
    c1, c2 = data[2], data[3]   
    # 切片拼图魔法：左边原样 + 中间替换 + 右边原样
    a = a[:l-1] + a[l-1:r].replace(c1, c2) + a[r:]
print(a)
```

> 注意切片是左闭右开，是浅拷贝，是从0开始

<a name="note-tsingpigdadademoban-14"></a>

### 字典与频次统计

默认值、字符权重与频次草稿。dict.get 的默认值应以位置参数传入，Couter 是原稿的拼写

```python
d.get(key,default_value=None)# 返回 key 对应的 value，不存在则返回 default_value
d.values()
d.items()
d=defaultdict(list)
d=defaultdict(int)
dict=[i-ord('a')+1 for i in range(ord('a'),ord('z')-1)]

##2606牛客
dict1=dict(zip(chars,vals))
for x in s:
    y=dict1.get(x,default_value=ord(x)-ord('a')+1)

arr=[a,a,a,bdf,df,]
c=Couter(arr)
print(c.most_common(2))
```

循环中使用 Counter 的笔记

> 杀手六：Counter可以一次性用但别丢循环里

根据四个选项的长度与极值出现次数作选择

```python
T=int(input())
se={0:'A',1:'B',2:'C',3:'D'}
for _ in range(T):
    s=[0]*4
    for i in range(4):
        s[i]=len(input())
    if s.count(max(s))==1 and s.count(min(s))!=1:
        print(se[s.index(max(s))])
    elif     s.count(min(s))==1 and s.count(max(s))!=1:
        print(se[s.index(min(s))])
    else:
        print('C')
```

字典查询旧值、写入新值并累计加权结果

```python
import sys
MOD=1<<64
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    f={}
    s=0
    for i in range(1,n+1):
        x,y=int(next(da)),int(next(da))
##        if x not in f:
##            f[x]=0
        v=f.get(x,0)
        s=(s+v*i)%MOD
        f[x]=y
    print(s)        
            
if __name__ == "__main__":
    solve()
```

用 Counter 判断两串的字符频次是否一致

```python
class Solution:
    def isCongruent(self , s: str, c: str) -> int:
        # 【架构升级】：O(1) 的极速前置拦截！
        # 如果长度都不一样，连建字典的资格都没有，直接斩立决
        if len(s) != len(c):
            return -1
            
        from collections import Counter
        # 【修复 2】：不要覆盖原变量，直接拿来比对
        if Counter(s) == Counter(c):
            # 【修复 1】：返回原字符串的长度
            return len(s)
            
        return -1
```

按字符需求比较可用数量的草稿

```python
class Solution:
    def canConstruct(self , ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        rr=set(ransomNote)
        r,m=Counter(ransomNote),Counter(magazine)
        flag=0
        for v in rr:
            if r[v]>m[v]:
                flag=1
                return False
        if flag==0:
            return False
```

<a name="note-tsingpigdadademoban-39"></a>

### 表达式与可迭代对象

range 长度与按条件调用 lambda 的速记

```python
length=[(end-start)//step]针对range(start,end,step)

(lambda :print('no'),lambda :print('yes'))[sum(l)/len(l)<60]()末尾括号立马调用函数
```

过滤含 4 的数和 4 的倍数。此行的 map 与 filter 括号仍是草稿

```python
a='\n'.join(map(str(x),filter(lambda x: x%4!=0 and '4' not in str(x)),range(1,n+1)))
```

按平均分选择输出，比较条件表达式与 lambda

```python
##牛牛是否被叫家长
l=list(map(int,input().split()))
##法一
##print("YES" if sum(l)/len(l)<60 else "NO")
##法二 
(lambda:print("NO"),lambda:print('YES'))[sum(l)/len(l)<60]()
##4. (lambda: print("NO"), lambda: print("YES"))[(a + b + c) / 3 < 60]()
##功能：根据平均值是否小于60，输出 "YES" 或 "NO"。
##分解：
##(lambda: print("NO"), lambda: print("YES"))：
##创建一个包含两个匿名函数的元组，索引0的函数输出 "NO"，索引1的函数输出 "YES"。
##[(a + b + c) / 3 < 60]：计算平均值并与60比较，得到布尔值。
##在Python中，True 等价于整数 1，False 等价于 0，
##因此该表达式的结果为 0 或 1，用作元组的索引。
##选中对应的lambda函数后，末尾的 () 立即调用该函数，执行 print(...)。
```

过滤含 4 的数与 4 的倍数，比较循环与 filter

```python
##牛牛数数
n=int(input())
##print(i) if str(i).count(4)==0 and i%4!=0 for i in range(1,n+1)
##str(i).count(4) 类型不匹配
##if...else 三元表达式的格式是 值1 if 条件 else 值2
##（只能返回 “值”，不能直接执行打印）
# 先判断整除（更快），再判断数字（避免无效的字符串转换）
for i in range(1,n+1):
    if i%4!=0 and '4' not in str(i):
        print(i)

##法二
##filter(function, iterable)
##保留 function(x) 为 True 的元素
##filter(lambda x:x%2==0, range(1,6))
##lambda 参数:表达式
##lambda x:x+1
##def f(x):
##    return x+1
##map(function, iterable)对每个元素应用函数。
n=int(input())
a='\n'.join(map(str,filter(lambda x:x%4!=0 and '4' not in str(x),range(1,n+1))))
print(a)
```

map 对象与常见迭代器

```python
s=[1,2,3,4]
print(type(map(int,s[:2])))
```

> 最常用、最容易碰到的迭代器就是：
> 👉 map /filter/zip /enumerate/reversed / 生成器表达式

用字典映射和差值判断胜平负

```python
a = {'elephant': 4, 'tiger': 3, 'cat': 2, 'mouse': 1}
s1, s2 = input().split()

diff = a[s1] - a[s2]

if diff == 1 or diff == -3:
    print('win')
elif diff == -1 or diff == 3:
    print('lose')
else:
    print('tie')
```

<a name="note-rthsrth-1"></a>

### 字符串赋值与循环

变量重新绑定与持续输出实验。原稿的 while True 会一直打印

```python
a='abc'

b=a
a='def'
while True:
    print('陈文静是大美女')
```

<a name="knowledge-params"></a>

### 函数参数与运算符映射

位置参数和关键字参数的打包速记

```python
def hanshu(*args)#未知个参数打包成元组
def han(**args)#未知个关键字参数打包成字典
```

通过字典按运算符取出函数的草稿

```python
op={'+':lambda a,b=a+b}
op[key](a,b)
```

<a name="knowledge-season"></a>

### 月份与条件分支

从输入中取出月份，判断对应季节

```python
## 四季
##法一
a=input()
# 提取月份
num=int(a[-2:])
####法二
##a=int(input())
##num=a%100
if 3<=num<=5:
    print('spring')
elif 6<=num<=8:
    print('summer')
elif 9<=num<=11:
    print('autumn')
elif 1<=(num%12)<=2:
    print('winter')
```

<a name="knowledge-matrix"></a>

### 矩阵遍历与网格模拟

按列输出矩阵转置，并记录运行时间

```python
import sys
import time
# 修正 1：正确的 readline 覆盖
input = sys.stdin.readline
def solve():
    # 读取第一行的 n 和 m
    n, m = map(int,input().split()) 
    lst=[list(map(int,input().split())) for _ in range(n)]
    for i in range(m):
        for j in range(n):
            print(lst[j][i],end=' ')
        print()
if __name__ == '__main__':
    # 性能测试计时器完美应用
    st = time.perf_counter()
    solve()
    ed = time.perf_counter()   
    # 打印运行时长（记得加换行，以免和上面的输出粘在一起）
    print(f"\n[性能测试] 运行耗时: {ed - st:.6f} 秒")
```

检查主对角线下方是否全为零

```python
import sys
import time
input=sys.stdin.readline
def solve():
    n=int(input())
    flag=0
    for i in range(n):
        s=list(map(int,input().split()))
        for j in range(0,i):
            if s[j]!=0:
                flag+=1
                break
    if flag==0:
        print('YES')
    else:
        print('NO')
if __name__ =='__main__':
    st=time.perf_counter()
    solve()
    ed=time.perf_counter()
    print(ed-st)
```

扫雷：填充边界后统计八邻域

```python
import sys
import time
input=sys.stdin.readline
def solve():
    n,m=map(int,input().split())
    arr=[[0]*(m+2) for i in range(n+2)]
    for i in range(n):
        s=list(input())
        for j in range(m):
            arr[i+1][j+1]=s[j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[i][j]=='*':
                print('*',end='')
                continue
            print([arr[i-1][j-1],arr[i-1][j],arr[i-1][j+1],arr[i][j-1],arr[i][j+1],arr[i+1][j-1],arr[i+1][j],arr[i+1][j+1]].count('*'),end='')
            
        print()
        
if __name__ =='__main__':
    st=time.perf_counter()
    solve()
    ed=time.perf_counter()
    print(ed-st)
```

<a name="knowledge-rot"></a>

### 字母表循环移位

字典映射的错误尝试

> 错误

```python
a=list('abcdefghijklmnopqrstyvwxyz')
s={a[i]:i+1  for i in range(26)}
n=int(input())
ss=list(input())
for i in range(len(ss)):
    ss[i]=s.value(s.value(ss[i])+n)
```

在字母表查索引，移位后按 26 取模

```python
n = int(input())
ss = input().strip() # 加上 strip 防止末尾的回车符捣乱
 1. 准备标准参照表（这次别再拼错了哈哈）
alpha = 'abcdefghijklmnopqrstuvwxyz'
ans = []
for char in ss:
    # 2. 找到当前字母在表里的索引 (a是0, b是1... z是25)
    current_idx = alpha.index(char)   
    # 3. 核心密码学公式：(当前位置 + 偏移量) 对 26 取模
    new_idx = (current_idx + n) % 26   
    # 4. 把加密后的字母塞进结果列表
    ans.append(alpha[new_idx])
 5. 拼接输出
print("".join(ans))
```

用 ord 和 chr 转换字符

```python
n = int(input())
ss = input().strip()
ans=[]
for x in ss:
    ans.append(chr((ord(x)-ord('a')+n)%26+ord('a')))
print(''.join(ans))
```

<a name="knowledge-sort"></a>

### 列表插入、排序与索引

插入元素、排序及列表输出格式

```python
s.insert(index=i+1,x)
s=sorted(s)
s.sort(reverse=True)
print(*s)
print(str(s).strip('[]').replace(',',''))#注意这里不要空格哈，因为元组字典列表啥的
逗号后面自带一个空格
```

保留原下标排序与逗号分隔输出

```python
arr=list(enumerate(map(int, input().split())))
arr.sort(key=lambda x:x[1])
for i in range(len(arr)):
    if arr[i][0]

s=list(map(int,input().split()))
print(str(s).strip('[]').replace(', ',','))
```

<a name="topic-io"></a>

## 竞赛输入输出与文件

先看标准输入的入口，再对照读文件、重定向和逐行解析的写法。

- [竞赛快读与输出](#note-tsingpigdadademoban-1)
- [本地文件与标准流切换](#note-tsingpigdadademoban-882)
- [文件题的读写方式](#note-tsingpigdadademoban-920)
- [输出分隔符与数值格式](#knowledge-print)

<a name="note-tsingpigdadademoban-1"></a>

### 竞赛快读与输出

读入整数的入口

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
if __name__=='__main__':
    solve()
```

依次读取网格元素与批量输出

```python
grid=[int(next(da)) for _ in range(m) for _ in range(n)]

sys.stdout.write('\n'.join(out)+'\n')
```

逐行读取与 strip 的两次练习

```python
import sys
for line in sys.stdin:
    line=line.strip()

for line in sys.stdin:
    line=line.strip()
```

DFS 练习文件中的输入骨架

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
if __name__=='__main__':
    solve()
```

单行、多行、矩阵与多组测试的输入写法

```python
#快读模板:写在前面用于加速
import sys
input=sys.stdin.readline

#一行多个整数
a,b,c=map(int,input().split())
nums=list(map(int,input().split()))

#n+n行每行一个数
n=int(input())
for _ in range(n):
    x=int(input())
    
#n+n行多个数
n=int(input())
for _ in range(n):
    nums=list(map(int,input().split()))

#n*m矩阵
n,m=map(int,input().split())
grid=[]
for _ in range(n):
    row=map(int,input().split())
    grid.append(row)
#or
n,m=map(int,intput().split())
grid=[list(map(int,input().split())) for _ in range(n)]

##多组数据
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
```

一次性读取多组数据并移动游标

```python
##更快读取所有数据，一次性!!!!!!!!!!!!!!!
import sys
data=sys.stdin.read().split()
t=int(data[0])
index=1
for _ in range(t):
    n,k=data[index],data[index+1]
    index+=2
    a=list(map(int,data[index:index+n]))
    index+=n
```

读入 T 组数据，用游标取出每组的整数

```python
##快速模板    
import sys
def solve():
    d=sys.stdin.read().split()
    T=int(d[0])
    out=[]
    id=1
    for  _ in range(T):
        n=int(d[id])
        id+=1
        a=[int(x) for x in d[id:id+n]]
        id+=n
        ans=sum(a)
        out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__ =='__main__':
    solve()
```

补充空输入判断的多组求和版本

```python
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    T=int(d[0])
    out=[]
    id=1
    for _ in range(T):
        n=int(d[id])
        id+=1
        a=[int(x) for x in d[id:id+n]]
        id+=n
        ans=sum(a)
        out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

持续按两个数一组读到输入末尾的草稿

```python
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    num=len(d)
    id=0
    out=[]
    while id<len(d):
        a,b=int(d[id]),int(d[id+1])
        id+=2
        ans=sum(a,b)
        out.append(str(ans))
    sys.stdout.write('\n'.join(out)+'\n')
if __name__ =='__main__':
    solve()
```

按行读取矩阵并累计元素和

```python
import sys
def solve():
    n,m=map(int,input().split())
    ans=0
    out=[]
    for line in sys.stdin:
        ans+=sum(map(int,line.split()))
    out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

<a name="note-tsingpigdadademoban-882"></a>

### 本地文件与标准流切换

检测 in.txt 后重定向输入、输出

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

### 文件题的读写方式

用 with 同时管理输入输出，保留两种写答案的方法

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

<a name="knowledge-print"></a>

### 输出分隔符与数值格式

print 的分隔符、结束符、列表展开与浮点精度

```python
print(value1,value2,value3,...,sep='分隔符')#自定义分隔符
print(value1,value2,value3,...,end='结束符，默认是换行，换成空格就是不换行')
#自定义结束符
print(f'字符若干{占位对象变量}')
print('{:格式}'.format(占位对象变量))#print("{:.3f}".format(x))
print(format(变量名,'格式'))#print(format(x,'.3f'))
print('%格式'%(变量名))##print('%.3f'%(x))
print(*lst)#快速输出列表
# 用f-string等价写法
print(f"{d3:.9f}")         # 输出 3.141592654
print(format(d3, ".9f"))
#format() 函数本身有专属的格式语法（不用 %），正确写法是去掉 %，直接写 .9f
```

保留三位小数的三种写法

```python
##浮点数###################################################################
x=float(input())
##法一
print('%.3f'%(x))

##法二
print(format(x,'.3f'))

##法三
print("{:.3f}".format(x))
```

复读机练习

```python
##复读机#######################################################################
for i in range(5):
    a=input()
    if i==c:
        print('.f'%(a))
    else:
        print(a)
```

手动插入千分位逗号与格式说明符

```python
N=list(input())
a=len(N)//3
flag=0
for i in range(1,a+1):
    N.insert(-i*3-flag,',')
    flag+=1
print(('').join(N))

print(f'{N:,}')
```

<a name="topic-structure"></a>

## 数据结构与计数

用集合删去已处理的元素，用频次表记录配对次数，或用抵消计数维护候选值。

- [多数元素与摩尔投票](#note-tsingpigdadademoban-95)
- [哈希集合与连续序列](#note-tsingpigdadademoban-245)
- [从双倍数组还原](#note-tsingpigdadademoban-263)
- [并查集与连通分量](#knowledge-union)
- [约瑟夫环与循环下标](#knowledge-joseph)
- [集合查找、交集与去重](#knowledge-membership)
- [栈与队列的基本操作](#knowledge-stack)
- [优先队列与前 K 项](#knowledge-heap)
- [栈与括号匹配](#knowledge-bracket)
- [栈顶合并与字符消除](#knowledge-cancel)
- [栈与表达式求值](#knowledge-expr)
- [进栈与出栈顺序](#knowledge-stackseq)
- [排队模拟与计数](#knowledge-queue)
- [先进先出缓存](#knowledge-fifo)
- [哈希配对与计数](#knowledge-pair)

<a name="note-tsingpigdadademoban-95"></a>

### 多数元素与摩尔投票

复杂度笔记

> 这道题的官方名字叫摩尔投票法。它把时间和空间复杂度压榨到了人类的物理极限：
> O(N)时间，O(1)空间。

计数抵消法，前提是多数元素存在。原稿缩进使用了全角空格

```python
def majorityElement(nums):
　　candidate = None
　　count = 0
　　
　　for x in nums:
　　　　if count == 0:
　　　　　　candidate = x
　　　　　　count = 1
　　　　elif x == candidate:
　　　　　　count += 1
　　　　else:
　　　　　　count -= 1
　　　　　　
　　return candidate
```

<a name="note-tsingpigdadademoban-245"></a>

### 哈希集合与连续序列

从未处理的数向两侧扩展，删除属于同一段的元素

```python
def longestConsecutive(self, nums: List[int]) -> int:
    s = set(nums)
    res = 0
    for x in nums:
        if x not in s: continue
        cur = 1
        s.remove(x)
        y = x + 1
        while y in s:
            s.remove(y)
            cur, y = cur + 1, y + 1
        y = x - 1
        while y in s:
            s.remove(y)
            cur, y = cur + 1, y - 1
        res = max(res, cur)
    return res
```

<a name="note-tsingpigdadademoban-263"></a>

### 从双倍数组还原

排序后二分寻找一半，逐对移除

```python
from bisect import *
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1: return []
        changed.sort()
        ans=[]
        while changed:
            x=changed[-1]
            if x&1:
                return []
            idx=bisect(changed,x//2)-1
            if idx==len(changed) or changed[idx]*2!=x:
                return []
            changed.remove(x//2)
            changed.remove(x)
            ans.append(x//2)
        return ans
```

用 Counter 沿倍数链扣除配对次数，单独处理零

```python
from bisect import *
from collections import *
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1: return []
        cnt=Counter(changed)
        ans=[]
        for i ,x in enumerate(changed):
            if cnt[x]==0:continue#漏了，核心就是处理所有cnt，循环动力
            if x==0:
                if cnt[x]&1 :return []
                else:
                    ans.extend([0]*(cnt[0]//2))
                cnt[x]=0
            while not x&1 and cnt[x//2]>0:#cnt[x//2]>0，腾都没了怎么摸瓜
                x//=2
            y=x
            while cnt[y]:#漏了，核心就是处理所有cnt，循环动力
                if cnt[2*y]<cnt[y]:
                    return []
                ans.extend([y]*cnt[y])
                cnt[y*2]-=cnt[y]
                cnt[y]=0

                if cnt[y*2]:
                    y=2*y
                else:
                    y=4*y
        return ans
```

<a name="knowledge-union"></a>

### 并查集与连通分量

父节点、合并集合与路径压缩

```python
fa=list(range(n))
#查x所在集合
def find(x):
    return x if fa[x]==x else find(fa[x])
#把小并入大
def union(da,xiao):
    if find(da)!=find(xiao):
        fa[find(xiao)]=find(da)
#路径压缩，全指向根节点(不严格！不完全，可能会漏)
def find(x):
    if fa[x]==x:return x
    fa[x]=find(fa[x])
    return fa[x]
```

多组边输入，统计连通分量的练习草稿

```python
import sys
input=lambda:sys.stdin.readline().strip()
def solve():
    while True:
        s=input()
        if s=='0':
            break
        m,n=map(int,s.split())
        fa=list(range(n+1))
        def find(x):
            if fa[x]==x:return x
            fa[x]=find(fa[x])
            return find(fa[x])
        def union(u,v):
            if find(u)!=find(v):
                fa[find(v)]=find(u)
        for _ in range(m):
            u,v=map(int,input().split())
            union(u,v)
        for _ in range(1,n+1):
            f[i]=find(i)
        cnt=len(set(fa))-1
        print(cnt-1)
```

<a name="knowledge-joseph"></a>

### 约瑟夫环与循环下标

用列表移除当前下标对应的元素

```python
n,k,m=map(int,input().split())
s=[i for i in range(n)]
while len(s)>1:
    s.remove(s[(k+m-1)%n])
    k=k+m-1
print(*s)
```

双端队列旋转与列表下标取模

```python
##法一约瑟夫环
from collections import deque
n,k,m=map(int,input().split())
s=deque(range(n))
s.rotate(-k)
whlie len(s)>1:
    s.rotate(-(m-1))
    s.popleft()
print(s[0])
   
n,k,m=map(int,input().split())
s=list(range(n))
while len(s)>1:
    k=(k+m-1)%len(s)
    s.pop(k)
print(s[0])
```

按当前位置的步长循环跳转

```python
s=list(map(int,input().split()))
m=s.pop()
idx=0
for i in range(m):
    idx=(idx+s[idx])%len(s)
print(idx+1)
```

<a name="knowledge-membership"></a>

### 集合查找、交集与去重

列表与集合查找的复杂度笔记

> 警惕sum、min、max、insert、pop、remove、list.count：O(N)
> in在列表找人:O(A*B),那In改成什么？列表转集合再用In在集合或字典找人
> eg:

```python
mt=[1,2,...,100000]
for target in qlist:
    for target in mt:
        pass:O(N**2)
mt=set(mt)
for target in qlist:
    for target in mt:
        pass:O(N)
```

用集合统计不同字符串的个数

```python
import sys
from collections import Counter
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    s=[next(da) for _ in range(n)]
    s=set(s)
    print(len(s))
    
if __name__ == "__main__":
    solve()
```

求两个数组的交集并排序

```python
class Solution:
    def intersection(self , nums1: List[int], nums2: List[int]) -> List[int]:
        i1=set(nums1)
        i2=set(nums2)
        i3=list(set.intersection(i1,i2))
        i3.sort()
        return i3
```

再写一遍字符串去重计数

```python
import sys
from collections import Counter
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    s=[next(da) for _ in range(n)]
    s=set(s)
    print(len(s))
    
if __name__ == "__main__":
    solve()
```

分组读取字符串再做去重的草稿

```python
import sys
from collections import Counter
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    a=[]
    for i in range(n):
        nu=int(next(da))        
        s=[next(da) for _ in range(nu)]
        
    s=set(s)
    print(len(s))
    
if __name__ == "__main__":
    solve()
```

<a name="knowledge-stack"></a>

### 栈与队列的基本操作

栈和队列的容器选择

> 杀手五：致命Queue和LifoQueue(栈)；
> 解药：栈用list.append()进栈，list.pop()出栈；
> 队列只用collections.deque,append进队，popleft()出队

预分配数组和栈顶指针处理 push、pop、query、size

```python
import sys
def main() -> None:
    data = sys.stdin.read().split()
    ptr = 0
    output = []

    stack = [""] * 100000
    s_ptr = -1

    n = int(data[ptr])
    ptr += 1

    for _ in range(n):
        command = data[ptr]
        ptr += 1

        if command == "push":
            x = data[ptr]
            ptr += 1

            s_ptr += 1
            stack[s_ptr] = x
        elif command == "pop":
            if s_ptr > -1:
                s_ptr -= 1
            else:
                output.append("Empty")
        elif command == "query":
            output.append(stack[s_ptr] if s_ptr > -1 else "Empty")
        elif command == "size":
            output.append(f"{s_ptr + 1}")

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
```

用 deque 实现队列命令与空队列提示

```python
import sys
from collections import deque
def solve():
    data=sys.stdin.read().split()
##    data='''7
##1 10
##1 20
##3
##4
##2
##3
##2'''.split()
    n=int(data[0])
    idx=1
    du=deque()
    while idx<=len(data)-1:
        op=data[idx]
        if op=='1':
            idx+=1
            du.append(data[idx])
            idx+=1
        elif op=='2':
            if du :
                du.popleft()
            else:
                print('ERR_CANNOT_POP')
            idx+=1

        elif op=='3':
            if du :
                print(du[0])
            else:
                print('ERR_CANNOT_QUERY')
            idx+=1
                
        else:
            print(len(du))
            idx+=1
            
if __name__ =='__main__':
    solve()
```

从列表头删除元素的开销

```python
def pop(self):
    re=self.stack[0]
    del self.stack[0]  #del底层会把后面的数往前挪！！！！！
    return re
```

<a name="knowledge-heap"></a>

### 优先队列与前 K 项

建堆、入堆、出堆与负数模拟最大堆

> 杀手七：不要用bisect.insort(arr,x)维护动态有序列表；解药：import heapq
> 建堆：heapify(arr)将一个无序列表转最小堆（不要用heappush一个个加进去建堆）O(N)
> 入堆：heappush(arr,val)冒泡上去O(logN)
> 出堆：heappop(arr)弹出并返回堆里最小元素（arr[0]）O(logN)
> 动态获取最大值：

```python
import heapq
nums=list(range(1000))
nums1=[-x for x in nums]
heapq.heapify(nums1)
```

用元组同时保存距离和节点

> 注意heapq还支持元组！

```python
import heapq
pq = []
# 存储格式：(距离, 节点编号)
heapq.heappush(pq, (10, 'A'))
heapq.heappush(pq, (2, 'B'))
heapq.heappush(pq, (5, 'C'))
# 弹出的绝对是距离最短的节点 B
distance, node = heapq.heappop(pq)
print(f"最近的节点是 {node}，距离 {distance}")
```

nlargest 与 nsmallest 选取前 K 项

> 如果题目是：“从 100 万个乱序数字中，找出最大的 5 个数”。不要去 sort()！
> 排序是 $O(N \log N)$。直接用 heapq 的内建高级函数，
> 时间复杂度降维至 $O(N \log K)$。Pythonimport heapq

```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 瞬间拿到最大的 3 个数，底层维护了一个大小只有 3 的小顶堆扫描全局！
top3_max = heapq.nlargest(3, nums)
print(top3_max)  # 输出: [42, 37, 23]
# 瞬间拿到最小的 3 个数
top3_min = heapq.nsmallest(3, nums)
print(top3_min)  # 输出: [-4, 1, 2]
```

<a name="knowledge-bracket"></a>

### 栈与括号匹配

按右括号分别判断圆括号与方括号

```python
s=input()
st=[]
flag=0
for x in s:
    if x=='(' or x=='[':
        st.append(x)
    elif x==')':
        if not st:
            print('false')
            flag=1
            break
        if st.pop()!='(':
            print('false')
            flag=1
            break
    elif x==']':
        if not st:
            print('false')
            flag=1
            break
        if st.pop()!='[':
            print('false')
            flag=1
            break
if flag==0:
    if not st:
        print('true')
    else:
        print('false')
```

用字典保存两类括号的配对关系

```python
s=input()
st=[]
flag=0
ma={')':'(',']':'['}
for x in s:
    if x=='(' or x=='[':
        st.append(x)
    elif x in ')]':
        if not st or st.pop()!=ma[x]:
            flag=1
            break
if flag == 0 and not st:
    print('true')
else:
    print('false')
```

把字典配对扩展到三种括号

```python
s=input()
st=[]
flag=0
ma={')':'(',']':'[','}':'{'}
for x in s:
    if x in '([{':
        st.append(x)
    elif x in ')]}':
        if not st or st.pop()!=ma[x]:
            flag=1
            break
if flag == 0 and not st:
    print('true')
else:
    print('false')
```

<a name="knowledge-cancel"></a>

### 栈顶合并与字符消除

字符 o 与 O 的消除初稿

> 错误

```python
s=input()
st=[]
flag=0
for x in s:
    if x=='o':
        if not st or st[-1]=='O':
            st.append(x)
        else:
            st.pop()
            st.append('O')
    else:
        if not st or st[-1]=='o':
            st.append(x)
        else:
            st.pop()
print(*st,end='')
```

入栈后反复检查栈顶并合并

> 无脑压栈+栈顶while循环消消乐

```python
s=input()
st=[]
for x in s:
    st.append(x)
    while len(st)>=2:
        if st[-1]=='o' and st[-2]=='o':
            st.pop()
            st.pop()
            st.append('O')
        elif st[-1]=='O' and st[-2]=='O':
            st.pop()
            st.pop()
        else:
            break
print(*st,end='')
```

<a name="knowledge-expr"></a>

### 栈与表达式求值

后缀表达式求值的初稿

```python
##错误
s=input()
st=[]
for i in range(len(s)):
    if s[i] not in '+-*':
        st.append(s[i])
        i+=2
    else:
        b=st.pop()
        a=st.pop()
##错误        st.append(eval(a s[i] b))
print(*st)
```

以 # 结束一个整数，再按运算符弹出两个操作数

```python
str=input()
st=[]
nu=''
for x in str:
    if x.isdigit():
        nu+=x
    elif x=='#':
        st.append(int(nu))
        nu=''
    elif x in '+-*':
        b=st.pop()
        a=st.pop()
        if x == '+':
            st.append(a + b)
        elif x == '-':
            st.append(a - b)
        elif x == '*':
            st.append(a * b)
return st[0]
```

加减乘和括号的计算器速记

```python
##应对包含 + - * 和括号的计算器
##“只把加法入栈，遇到乘法就吃掉栈顶，遇到括号就丢给递归！”
print(eval(s))
```

<a name="knowledge-stackseq"></a>

### 进栈与出栈顺序

用后缀最大值决定何时弹出栈顶

```python
##只要我手里的牌（栈顶），
##比桌面上所有剩下的牌（未来最大值）都要大，我就立刻打出！
##否则，我就继续憋着抓牌。

import sys
def solve():
    data=sys.stdin.read().split()
    n=int(data[0])
##    p=list(data[1:])
    p=[int(x) for x in data[1:]]
    ma=[0]*(n+1)
    for i in range(n-1,-1,-1):
        ma[i]=max(p[i],ma[i+1])
    re=[]
    st=[]
    for i in range(n):
        st.append(p[i])
        while st and st[-1]>ma[i+1]:
            re.append(str(st.pop()))
    print(' '.join(re))
if __name__ =='__main__':
    solve()
```

给定入栈序列，模拟并验证出栈序列

```python
import sys
def solve():
    data=sys.stdin.read().split()
##    data='''2
##5
##1 2 3 4 5
##2 5 4 1 3
##5
##1 2 3 4 5
##2 5 4 3 1'''.split()
    q=int(data[0])
    idx=1
    for i in range(q):
        n=int(data[idx])
        idx+=1
        pu=[int(x) for x in data[idx:idx+n]]
        idx+=n
        po=[int(x) for x in data[idx:idx+n]]
        idx+=n
        re=[]
        p=0
        for x in pu:
            re.append(x)
            while re and re[-1]==po[p]:
                re.pop()
                p+=1
        if  not re:
            print('Yes')
        else:
            print('No')
if __name__ =='__main__':
    solve()
```

<a name="knowledge-queue"></a>

### 排队模拟与计数

学生与三明治：队列轮转

```python
class Solution:
    def countStudents(self , students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        q=deque(students)
        for s in sandwiches:
            re=0
            while q and q[0]!=s:
                if re == len(q):
                    return len(q)
                
                q.append(q.popleft())
                re+=1
            if q:    
                q.popleft()
        return 0
```

学生与三明治：只维护两种偏好的剩余人数

```python
class Solution:
    def countStudents(self , students: List[int], sandwiches: List[int]) -> int:
        count={0:students.count(0),1:students.count(1)}
        for s in sandwiches:
            if count[s]>0:
                count[s]-=1
            else:
                break
        return count[0]+count[1]
```

买票耗时：队列记录位置与剩余票数

```python
class Solution:
    def timeRequiredToBuy(self , tickets: List[int], k: int) -> int:
        from collections import deque
        q=deque((i,tickets) for i,tickets in enumerate(tickets))
        ti=0
        while q:
            idx,cnt=q.popleft()
            cnt-=1
            ti+=1
            if cnt==0 and idx==k:
                return ti
            if cnt>0:
                q.append((idx,cnt))
        return ti
```

买票耗时：逐人计算对总时间的贡献

```python
class Solution:
    def timeRequiredToBuy(self , tickets: List[int], k: int) -> int:
        t=tickets[k]
        ti=0
        for i in range(len(tickets)):
            if i<=k:
                ti+=min(tickets[i],t)
            else:
                ti+=min(tickets[i],t-1)
        return ti
```

买票耗时：循环下标模拟

```python
class Solution:
    def timeRequiredToBuy(self , tickets: List[int], k: int) -> int:
        idx=0
        ti=0
        while tickets[k]!=0:
            if tickets[idx]>0:
                tickets[idx]-=1
                ti+=1
                idx+=1
            else:
                idx+=1
            idx%=len(tickets)
        return ti
```

买票耗时：按下标排队并扣减票数

```python
class Solution:
    def timeRequiredToBuy(self , tickets: List[int], k: int) -> int:
        from collections import deque
        nu=deque(range(len(tickets)))
        ti=0
        while True:
            ti+=1
            i=nu.popleft()
            if tickets[i]>1:
                tickets[i]-=1
                nu.append(i)
            else:
                if i==k:
                    return ti
```

按阵营人数推演胜负的草稿

```python
class Solution:
    def predictVictory(self , s: str) -> str:
        r,d=s.count('R'),s.count('D')
        for x in s:
            if r==0:
                return 'Dark'
            elif d==0:
                return 'Red'
            if x=='D':
                r-=1
            else:
                d-=1
```

<a name="knowledge-fifo"></a>

### 先进先出缓存

有限容量队列中统计缺失次数

```python
import sys
from collections import deque
def solve():
    data=sys.stdin.read().split()
    m=int(data[0])
    n=int(data[1])
    s=[int(x) for x in data[2:3+n]]
    du=deque()
    mi=0
    for i in range(n):
        if s[i] not in du:
            if len(du)<m:
                du.append(s[i])
                mi+=1
            else:
                du.popleft()
                du.append(s[i])
                mi+=1
    print(mi)
            
if __name__ =='__main__':
    solve()
```

<a name="knowledge-pair"></a>

### 哈希配对与计数

用频次乘积统计差值等于 C 的数对

```python
import sys
from collections import Counter
def solve():
    da=iter(sys.stdin.read().split())
    n,c=int(next(da)),int(next(da))
    s=[int(next(da)) for _ in range(n)]
    ss=Counter(s)
    ans=0
##    for i in ss:
##        for j in ss:
##            if i-j==c:
##                ans+=ss[i]+ss[j]
##    print(ans)
    for j in ss:
        i=j+c
        if i in ss:
            ans+=ss[i]*ss[j]
    print(ans)

if __name__ == "__main__":
    solve()
```

两数之和：查找补数并返回下标

```python
class Solution:
    def twoSum(self , nums: List[int], target: int) -> List[int]:
        re={}
        for i,v in enumerate(nums,start=1):
            j=target-v
            if j not in re:
                re[v]=i
            else:
                return [re[j],i]
```

<a name="topic-greedy"></a>

## 贪心与堆

先确定处理顺序，再判断要保留哪项选择。反悔型题目用堆取出最值得撤回的一项。

- [排序与插入](#note-tsingpigdadademoban-87)
- [区间任务调度](#note-tsingpigdadademoban-112)
- [分段计算训练成本](#note-tsingpigdadademoban-129)
- [堆相关练习题号](#note-tsingpigdadademoban-155)
- [反悔贪心与堆](#note-tsingpigdadademoban-158)
- [利润与类别数的权衡](#note-tsingpigdadademoban-208)
- [工资比例与最大堆](#note-tsingpigdadademoban-228)
- [双指针配对](#note-tsingpigdadademoban-336)

<a name="note-tsingpigdadademoban-87"></a>

### 排序与插入

按身高降序、同身高按 k 升序重建队列

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans=[]
        for p in people:
            ans.insert(p[1],p)
        return ans
```

<a name="note-tsingpigdadademoban-112"></a>

### 区间任务调度

按结束时间排序，优先把开机时段安排在区间右端

```python
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1])        
        n=len(tasks)
        ed=tasks[-1][1]

        ip=[0]*(ed+1)
        for l,r,c in tasks:
            c-=sum(ip[l:r+1])
            if c>0:
                for i in range(r,l-1,-1):
                    if ip[i]:continue
                    ip[i]=1
                    c-=1
                    if c==0:break
        return sum(ip)
```

<a name="note-tsingpigdadademoban-129"></a>

### 分段计算训练成本

按所需次数分组，每段比较集训价格与剩余单价总和

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n,s=int(next(da)),int(next(da))
    p=[0]*n
    c=[0]*n
    sc=0
    for i in range(n):
        p[i],c[i]=int(next(da)),int(next(da))
        sc+=p[i]
    c,p=zip(*sorted(zip(c,p)))
    tg=0
    ans=0
    for i in range(n):
        if sc>=s:
            ans+=(c[i]-tg)*s
            
        else:
            ans+=(c[i]-tg)*sc
        tg=c[i]#处理了多少尸体
        sc-=p[i]

    print(ans)        
if __name__=='__main__':
    solve()
```

<a name="note-tsingpigdadademoban-155"></a>

### 堆相关练习题号

原稿记下的 LeetCode 1834 与 218

```python
##LeetCode 1834
##LeetCode 218
```

<a name="note-tsingpigdadademoban-158"></a>

### 反悔贪心与堆

课程安排。超过截止时间时撤回耗时最长的课

```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        hq=[]
        cur=0
        for d,l in courses:
            cur+=d
            heappush(hq,-d)
            if cur>l:
                cur+=heappop(hq)
        return len(hq)
```

魔塔。生命值不足时推迟已经遇到的伤害最大的一项

```python
from heapq import *
class Solution:
    def magicTower(self, nums: List[int]) -> int:       
        ans=0
        if sum(nums)+1<=0:
            return -1
        hq=[]
        cur=1
        for i,x in enumerate(nums):
            cur+=x
            if x<0:
                heappush(hq,x)
            if cur<=0:
               
                cur-= heappop(hq)
                ans+=1
        return ans
```

加油站。燃料不足时从已经过的站中补选油量最多的

```python
from heapq import *
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        stations.append([target,0])
        wz=0
        hp=[]
        curf=startFuel
        ans=0
        for p,f in stations:
            cost=p-wz
            curf-=cost
            wz=p
            while curf<0 and hp:
                curf-=heappop(hp)
                ans+=1
            if curf<0:#加完油还不够
                return -1
            heappush(hp,-f)
        return ans
```

<a name="note-tsingpigdadademoban-208"></a>

### 利润与类别数的权衡

先选利润最高的 k 项，再用新类别替换重复类别

```python
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        st=[]#返回站
        vip=set()#尊贵去
        tot=0
        res=0
        for i ,(p,c) in enumerate(items):
            if i<k:
                tot+=p
                if c not in vip:
                    vip.add(c)
                else:
                    st.append(p)
            elif st and c not in vip :
                tot+=p-st.pop()
                vip.add(c)
            res=max(res,tot+len(vip)**2)###########
        return res
```

<a name="note-tsingpigdadademoban-228"></a>

### 工资比例与最大堆

按工资质量比排序，用堆维护 k 人的质量总和

```python
from heapq import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        r=([wage[i]/quality[i] for i in range(len(wage))])
        lst=sorted(zip(r,quality))
        hp=[]
        sq=0
        ans=float('inf')
        for i,(ri,qi) in enumerate(lst):
            heappush(hp,(-qi,i))
            sq+=qi
            if len(hp)>k:
                sq+=heappop(hp)[0]
            if len(hp)==k:
                ans=min(ans,ri*sq)#娶不到
        return ans
```

<a name="note-tsingpigdadademoban-336"></a>

### 双指针配对

救生艇。让最重的人尝试与最轻的人同船

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort(reverse=True)
        x,y=0,n-1
        res=0
        while x<=y:
            remain=limit-people[x]
            x+=1
            if remain >=people[y]:
                y-=1
            res+=1
        return res
```

<a name="topic-difference"></a>

## 前缀和与差分

把一次区间更新记录在两个端点上，再通过前缀和恢复每个位置的覆盖次数。

- [区间覆盖与前缀和](#note-tsingpigdadademoban-350)
- [二分定位与差分计数](#note-reshensaibaiduzhixing-1)
- [三角数的前缀和](#knowledge-prefix)
- [闭区间覆盖与剩余点数](#knowledge-interval)
- [定长窗口的区间和](#knowledge-window)

<a name="note-tsingpigdadademoban-350"></a>

### 区间覆盖与前缀和

把每个数可调整的范围视为区间，用差分求最大重叠数

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n=len(nums)
        m=max(nums)
        t=[0]*(m+2*k+2)
        d=[0]*(m+2*k+2)
        cnt=0
        for i ,x in enumerate(nums):
            a,b=x,x+2*k
            t[a]+=1
            t[b+1]-=1
        for i in range(m+2*k+2):
            cnt+=t[i]
            d[i]+=cnt
        return max(d)
```

<a name="note-reshensaibaiduzhixing-1"></a>

### 二分定位与差分计数

百度之星热身赛。用左右二分定位闭区间，再按覆盖次数模 4 分组，含手写输入样例

```python
##import sys
##def solve():
##    da=iter(sys.stdin.read().split())
##    n=int(next(da)
##    
##if __name__=='__main__':
##    solve()


import sys
import bisect
def solve():
    da=iter(sys.stdin.read().split())
##    da=iter('''3 4
##2 5 1
##1 3
##2 2
##2 2
##2 2
##'''.split())
    n,m=int(next(da)),int(next(da))
    si=[int(next(da)) for _ in range(n)]
    s=[float('-inf')]+sorted(si)+[float('inf')]
    deff=[0]*(n+2)
    diff=[0]*(n+2)
    for _ in range(m):
        l,r=int(next(da)),int(next(da))
        inl=bisect.bisect_left(s,l)
        inr=bisect.bisect_right(s,r)
        diff[inl]+=1
        diff[inr]-=1
##        print(inl,inr)
    d,nan,x,b=0,0,0,0
    ls=0
    for i in range(1,n+1):
        ls+=diff[i]
        deff[i]+=ls
        if deff[i]%4==0:d+=1
        elif deff[i]%4==1:nan+=1
        elif deff[i]%4==2:x+=1
        elif deff[i]%4==3:b+=1

    
    print(d,nan,x,b)
if __name__=='__main__':
    solve()
```

<a name="knowledge-prefix"></a>

### 三角数的前缀和

生成器、前缀数组、求和公式与 accumulate 的四种写法

```python
##牛牛学数列4
##法一：第一层用生成器
n=int(input())
s=sum(i*(i+1)//2 for i in range(1,n+1))
print(s)

##法二：基础前缀和
n=int(input())
prefix=[0]*(n+1)
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+i
ans=sum(prefix)
print(ans)

##法三：四面体数公式
n=int(input())
print(n*(n+1)*(n+2)//6)

##法四：高效前缀和
from itertools import accumulate
n=int(input())
ans=sum(accumulate(range(1,n+1)))
```

<a name="knowledge-interval"></a>

### 闭区间覆盖与剩余点数

方法一：集合记录被覆盖的点

```python
##法一：离散化点集合去重        
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    L=int(d[0])
    M=int(d[1])
    out=[]
    id=2
    t=set()
    for _ in range(M):
        l,r=int(d[id]),int(d[id+1])
        id+=2
        t.update(range(l,r+1))
    ans=L+1-len(t)        
    out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

方法二：逐点修改状态数组

```python
##法二：开状态数组，0表示被挖        
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    L=int(d[0])
    M=int(d[1])
    out=[]
    id=2
    t=[1]*(L+2)
    for _ in range(M):
        l,r=int(d[id]),int(d[id+1])
        id+=2
        for i in range(l,r+1):
            t[i]=0
    ans=sum(t)-1        
    out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

方法三：差分数组统计覆盖次数

```python
##法三：差分数组-消除区间循环       
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    L=int(d[0])
    M=int(d[1])
    out=[]
    id=2
    t=[0]*(L+2)    
    for _ in range(M):
        l,r=int(d[id]),int(d[id+1])
        id+=2
##        t[l]=-1
##        t[r+1]=1
        t[l]-=1
        t[r+1]+=1
    c=0
    ans=0
    for i in range(L+1):
        c+=t[i]
        if c==0:
            ans+=1        
    out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

方法四：排序并合并区间

```python
##法四：贪心归并区间      
import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    L=int(d[0])
    M=int(d[1])
    out=[]
    id=2
    ni=[]   
    for _ in range(M):
        ni.append([int(d[id]),int(d[id+1])])
        id+=2
    ni.sort()
    me=[]
    for nii in ni:
        if not me or nii[0]>me[-1][1]:
            me.append(nii)
        else:
            me[-1][1]=max(me[-1][1],nii[1])
    ans=L+1-sum(r-l+1 for l,r in me)
    out.append(str(ans))

    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

<a name="knowledge-window"></a>

### 定长窗口的区间和

每次切片求和与维护滑动窗口和

> 杀手二：毫无节制的切片；解药：双指针Or前缀和

```python
for i in range(n-k):
    currentsum=sum(arr[i:i+k])
currentsum=sum(arr[:k])
for i in range(1,n-k+1):
    currentsum=currentsum-arr[i-1]+arr[i+k-1]
```

<a name="topic-binary"></a>

## 二分与答案边界

先写出候选值的可行条件，再判断要找第一个可行值还是最后一个可行值。

- [冶炼金属的可行区间](#note-tsingpigdadademoban-366)
- [二分答案分糖果](#note-tsingpigdadademoban-466)
- [二分插入位置与比较键](#knowledge-bis)
- [有序集合的前驱与后继](#knowledge-ordered)
- [查找并删除最近元素](#knowledge-near)

<a name="note-tsingpigdadademoban-366"></a>

### 冶炼金属的可行区间

初稿。两处二分调用的括号未闭合

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=int(next(da)),int(next(da))
    def bst(lo,hi,check):
        while lo<hi:
            mid=(lo+hi)>>1
            if check(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
    m=bst(1,10**9,lambda v:all(c//v<=d for c,d in zip(a,b))
    M=bst(1,10**9,lambda v:any(c//v<d for c,d in zip(a,b))-1
        
if __name__=='__main__':
    solve()
```

带判定方向讲解的左右边界模板

```python
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
a, b = zip(*[map(int, input().split()) for _ in range(n)])
# ==========================================
# 【抽象 1：标准的 bisect_left 模板】
# 功能：在 [False, ..., False, True, True] 阵列中寻找第一个 True
# ==========================================
def bisect_left(lo, hi, check_left):
    while lo < hi:
        mid = (lo + hi) // 2
        if check_left(mid):
            hi = mid       # 如果是 True，说明当前点可能是第一个，或者第一个在左边，收缩右边界
        else:
            lo = mid + 1   # 如果是 False，说明太小了，第一个 True 必然在右边，步进左边界
    return lo
# ==========================================
# 【抽象 2：标准的 bisect_right 模板】
# 功能：在 [True, True, ..., True, False, False] 阵列中寻找第一个 False
# ==========================================
def bisect_right(lo, hi, check_right):
    while lo < hi:
        mid = (lo + hi) // 2
        if check_right(mid):
            # 语法规则：对应 Python 内置 bisect_right 的强盗逻辑。
            # 如果当前点是 True（合法），说明“第一个 False”必然在当前点的严格右侧！
            lo = mid + 1   
        else:
            # 如果当前点是 False（不合法），说明它有可能是第一个 False，
            # 或者第一个 False 在它的左侧，因此收缩右边界。
            hi = mid       
    return lo
# --- 核心调用逻辑 ---
# 1. 求最小值 m：寻找第一个让产量“不超标”的 v
# 状态阵列形态：[太小(False), 太小(False), 刚好(True), 太大(True)...]
m = bisect_left(1, 10**9, lambda v: all(A // v <= B for A, B in zip(a, b)))
# 2. 求最大值 M：寻找第一个让产量“缩水”的 v (即首个 False)
# 状态阵列形态：[太小(True), 刚好(True), 刚好(True), 太大(False), 太大(False)...]
# 这里的 check 条件变成了 >= B 
M_pos = bisect_right(1, 10**9, lambda v: all(A // v >= B for A, B in zip(a, b)))
# 因为 bisect_right 返回的是第一个 False 的坐标，所以最大合法的 True 坐标需要减 1
M = M_pos - 1
print(m, M)
```

快读版本，对比两个判定函数与返回边界

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=int(next(da)),int(next(da))
    def bl(lo,hi,check):
        while lo<hi:
            mid=(lo+hi)>>1
            if check(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
    def br(lo,hi,check):
        while lo<hi:
            mid=(lo+hi)>>1
            if check(mid):
                lo=mid+1
            else:
                hi=mid
        return lo-1    
    m=bl(1,10**9,lambda v:all(c//v<=d for c,d in zip(a,b)))
    M=br(1,10**9,lambda v:all(c//v>=d for c,d in zip(a,b)))
    print(m,M)    
    
if __name__=='__main__':
    solve()
```

<a name="note-tsingpigdadademoban-466"></a>

### 二分答案分糖果

枚举每人份量，按各堆能提供的份数判断可行性

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:return 0
        def br(lo,hi,check):
            while lo<hi:
                mid=(lo+hi)>>1
                if check(mid):
                    lo=mid+1
                else:
                    hi=mid
            return lo-1
        return br(0,max(candies)+1,lambda x:sum(i//x for i in candies)>=k)
#左闭右开模板，上界+1
```

<a name="knowledge-bis"></a>

### 二分插入位置与比较键

按比较键寻找右侧插入位置

```python
def bisect(a,x,lo=0,hi=None,check=lambda x:x):
    if hi is None:hi=len(a)
    while lo<hi:
        i=(lo+hi)>>1
        if check(a[i])>x:
            hi=i
        else:
            lo=i+1
    return lo
```

<a name="knowledge-ordered"></a>

### 有序集合的前驱与后继

集合负责判重，有序列表负责定位邻居

```python
import bisect

# 顶级设施：双轨制仓库
ms = set()
ml = []

def insertValue(x):
    if x not in ms:
        ms.add(x)
        bisect.insort(ml, x) # insort 内部自带二分插入，不用改

def eraseValue(x):
    if x in ms:
        ms.remove(x)  # 【修复 1】：用 remove 而不是 pop
        idx = bisect.bisect_left(ml, x) # 【修复 2】：精确找左边界
        # 严格防御：虽然 ms 里有，但养成好习惯确认一下再 pop
        if idx < len(ml) and ml[idx] == x: 
            ml.pop(idx)

def xInSet(x):
    # 【修复 3】：只负责返回布尔值，不负责 print
    return x in ms

def sizeOfSet():
    return len(ml)

def getPre(x):
    # 【修复 4】：正确调用函数并获取位置
    pos = bisect.bisect_left(ml, x)
    # 【修复 5】：边界拦截，如果是 0 说明左边没人了，返回题目要求的 -1
    if pos == 0:
        return -1
    return ml[pos - 1]

def getBack(x):
    # 找后继必须用 bisect_right 找严格大于的第一个位置
    pos = bisect.bisect_right(ml, x)
    # 边界拦截：如果到了数组长度，说明右边没人了
    if pos == len(ml):
        return -1
    return ml[pos]

def main():
    q = int(input())
    for _ in range(q):
        line = list(map(int, input().split()))
        op = line[0]
        x = line[1] if len(line) > 1 else 0
        
        # 网关层负责解析参数和调用服务
        if op == 1:
            insertValue(x)
        elif op == 2:
            eraseValue(x)
        elif op == 3:
            print("YES" if xInSet(x) else "NO")
        elif op == 4:
            print(sizeOfSet())
        elif op == 5:
            print(getPre(x))
        elif op == 6:
            print(getBack(x))

if __name__ == "__main__":
    main()
```

允许重复值的有序列表及计数接口

```python
import bisect
ms=[]
def insertValue(x):
    bisect.insort_right(ms,x)
    # TODO: 实现插入逻辑
    pass

def eraseValue(x):
    idx=bisect.bisect_left(ms,x)
    if idx<len(ms) and ms[idx]==x:
        ms.pop(idx)
    # TODO: 实现删除逻辑
    pass

def xCount(x):
    i1=bisect.bisect_left(ms,x)
    i2=bisect.bisect_right(ms,x)
    return i2-i1
    # TODO: 求x在集合中的个数
    pass

def sizeOfSet():
    return len(ms)
    # TODO: 返回集合大小
    pass

def getPre(x):#bisect.bisect_left:按升序找x插入的位置
    idx=bisect.bisect_left(ms,x)
    return ms[idx-1] if idx>0 else -1
    # TODO: 实现找前驱
    pass

def getBack(x):#bisect.bisect_right:比x大的第一个位置
    idx=bisect.bisect_right(ms,x)
    return ms[idx] if idx<len(ms) else -1
    
    # TODO: 实现找后继
    pass

def main():
    q = int(input())
    for _ in range(q):
        line = map(int,input().split())
        cnt,op,x=0,0,0
        for i in line:
            if(cnt==0):
                op=i
            else:
                x=i
            cnt+=1
        
        if op == 1:
            insertValue(x)
        elif op == 2:
            eraseValue(x)
        elif op == 3:
            print(xCount(x))
        elif op == 4:
            print(sizeOfSet())
        elif op == 5:
            print(getPre(x))
        elif op == 6:
            print(getBack(x))

if __name__ == "__main__":
    main()
```

<a name="knowledge-near"></a>

### 查找并删除最近元素

初稿：插入、寻找相邻值与删除

```python
##错误
import sys
import bisect
def solve():
    da=iter(sys.stdin.read().split())
    q=int(next(da))
    ms=set()
    ml=[]
    for _ in range(q):
        a,b=int(next(da)),int(next(da))
        if a==1:
            if b not in ms:
                ms.add(b)
                bisect.insort_right(ml,x)
            else:
                print('Already Exist')
        else:
           if ms:
               i1=bisect.bisect_left(ml,x)
               i2=bisect.bisect_right(ml,x)
               c1=ml[i1-1] if i1>0 else float(-inf)
               c2=ml[i2] if i2<len(ml) else float(inf)
               if c1<=c2:
                   ml.pop(i1-1)
                   ms.remove(ml[i1-1])
               else:
                   ml.pop(i2)
                   ms.remove(ml[i2])
            else:
                print('Empty')
if __name__ == "__main__":
    solve()
```

对照写法：比较两侧距离，记录胜者后更新集合与列表

```python
import sys
import bisect

def solve():
    da = iter(sys.stdin.read().split())
    # 防御性判断：如果输入为空直接退出
    try:
        q_str = next(da)
    except StopIteration:
        return
    q = int(q_str)
    
    ms = set()
    ml = []
    out = [] # 收集输出，统一打印
    
    for _ in range(q):
        a = int(next(da))
        b = int(next(da))  # 这里统一用 b 接收目标值
        
        if a == 1:
            if b not in ms:
                ms.add(b)
                bisect.insort_left(ml, b)
            else:
                out.append('Already Exist')
        else:
            if ms:
                # 只需要一个 bisect_left，就能囊括所有情况
                idx = bisect.bisect_left(ml, b)
                
                # 候选人1：左侧邻居（注意加上单引号的 '-inf'）
                c1 = ml[idx - 1] if idx > 0 else float('-inf')
                
                # 候选人2：右侧邻居（或者是 b 本身）
                c2 = ml[idx] if idx < len(ml) else float('inf')
                
                # 算距离！这是核心！
                d1 = abs(b - c1)
                d2 = abs(c2 - b)
                
                # 如果左边距离更近，或者距离一样（取较小值，即左边）
                if d1 <= d2:
                    winner = c1
                    win_idx = idx - 1
                else:
                    winner = c2
                    win_idx = idx
                
                # 记录结果
                out.append(str(winner))
                
                # 【关键操作】：一定是先在 set 里删掉 winner，再去动 list！
                # 这样就不会有索引错乱的问题
                ms.remove(winner)
                ml.pop(win_idx)
            else:
                out.append('Empty')

    # 最后一次性输出所有结果
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    solve() # 这里要调用 solve，而不是 main
```

<a name="topic-recurrence"></a>

## 递推与组合计数

同一道跳台阶题，从递归、滚动变量、特征方程和组合计数四个角度看。

- [跳台阶](#note-dfs-9)
- [线性递推与滚动变量](#knowledge-linear)
- [格点路径与组合数](#knowledge-paths)
- [杨辉三角](#knowledge-pascal)

<a name="note-dfs-9"></a>

### 跳台阶

题目与第一种思路

> ##跳台阶https://www.acwing.com/problem/content/823/
> 法一

递归求 f(n−1) 与 f(n−2) 的和

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    def check(n):
        if n==0:return 0
        elif n==1:return 1
        elif n==2:return 2
        else:
            return check(n-1)+check(n-2)
    print(check(n))
if __name__=='__main__':
    solve()
```

特征方程与迭代法的过渡笔记

> 法二：特征方程求解（c1+c2*n）*r^n或c1*r1^n+c2*r2^n
> 法三

用两个变量滚动更新相邻项

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    a,b=1,2
    for _ in range(n-1):
        a,b=b,a+b#fk,fk+1=fk+1,fk+2而fk+2=fk+fk+1
    print(a)
if __name__=='__main__':
    solve()
```

按走两级台阶的次数，枚举步序中的位置

> 法四：设走k个2级台阶，则走了2k步，剩下走n-2k个一级台阶，总共k+n-2k=n-k种选法，
> c(k,n-k)且k<=[n/2]

<a name="knowledge-linear"></a>

### 线性递推与滚动变量

三阶递推，比较递归与滑动更新

```python
##牛牛学数列6
n=int(input())
def a(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return a(n-3)+2*a(n-2)+a(n-1)
print(a(n))
##法二：滑窗思想
n=int(input())
a,b,c=0,1,1
for i in range(n-3):
    a,b,c=b,c,(a+2*b+c)
print(c)
```

<a name="knowledge-paths"></a>

### 格点路径与组合数

网格路径的组合数与一维滚动数组

```python
##二维斐波那契数列
n,m=map(int,input().split())
##法一：走到目的地方案数
import math
print(math.comb(n+m-2,n-1)%1000000007)
##从（1，1）到（n,m）要往下走n-1步，往右m-1

##法二：滑窗
dp=[1]*m
for _ in range(1,n):
    for j in range(1,m):
        dp[j]=dp[j]+dp[j-1]
print(dp[-1]%1000000007)
```

<a name="knowledge-pascal"></a>

### 杨辉三角

逐行递推并打印杨辉三角

```python
import sys
import time
input = sys.stdin.readline
def solve():
    n=int(input())
    dp=[[0]*n for i in range(n)]
    for i in range(n):
        dp[i][0]=dp[i][i]=1
        for j in range(1,i):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        row=dp[i][:i+1]
        print(*row)

if __name__ == '__main__':
    # 性能测试计时器完美应用
    st = time.perf_counter()
    solve()
    ed = time.perf_counter()   
    # 打印运行时长（记得加换行，以免和上面的输出粘在一起）
    print(f"\n[性能测试] 运行耗时: {ed - st:.6f} 秒")
```

<a name="topic-dfs"></a>

## DFS、枚举与回溯

从选或不选、排列和组合开始，再看怎样记录路径、限制下一层起点，以及何时恢复访问标记。

- [递归深度与缓存](#note-tsingpigdadademoban-37)
- [装箱与最少工作时段](#note-tsingpigdadademoban-313)
- [逐位搜索最大数](#note-tsingpigdadademoban-480)
- [记录方案与恢复现场](#note-tsingpigdadademoban-531)
- [组合枚举](#note-tsingpigdadademoban-558)
- [组合总和](#note-tsingpigdadademoban-574)
- [子集枚举](#note-dfs-39)
- [排列枚举](#note-dfs-79)
- [选数与素数和](#note-dfs-158)
- [烤鸡的定长枚举](#note-dfs-294)
- [火星人与字典序后继](#note-dfs-356)
- [火柴加法](#note-dfs-561)
- [配料的酸度与苦度](#note-dfs-610)
- [递归分支与终止条件](#knowledge-enum)

<a name="note-tsingpigdadademoban-37"></a>

### 递归深度与缓存

调整解释器的递归上限

```python
sys.setrecursionlimit(1000000)
```

记忆化装饰器片段

```python
@lru_cache(maxsize=None)
```

导入 functools 后使用 lru_cache

```python
from functools import *
@lru_cache(maxsize=None)
```

<a name="note-tsingpigdadademoban-313"></a>

### 装箱与最少工作时段

任务从大到小放入已有时段，或新开时段并回溯

```python
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)
        n=len(tasks)
        cnt=[0]*n
        res=float('inf')
        def dfs(i,cur):
            nonlocal res
            if cur>res:return 
            if i==n:
                res=cur
                return 
            for j in range(cur):
                if tasks[i]<=sessionTime-cnt[j]:
                    cnt[j]+=tasks[i]
                    dfs(i+1,cur)
                    cnt[j]-=tasks[i]
            cnt[cur]+=tasks[i]
            dfs(i+1,cur+1)
            cnt[cur]-=tasks[i]
        dfs(0,0)
        return res
```

<a name="note-tsingpigdadademoban-480"></a>

### 逐位搜索最大数

记录当前数位和两类剩余操作次数，探索各分支

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    N,a,b=next(da),int(next(da)),int(next(da))
    n=list(map(int,N))
    path=[]
    l=len(n)
    res=0
    def dfs(i,ra,rb):
        nonlocal res
        if len(path)==l:
            res=max(res,int(''.join(map(str,path))))
            return 
        d=min(9-n[i],ra)
        path.append(n[i]+d)
        dfs(i+1,ra-d,rb)
        path.pop()
        if rb>=n[i]+1:
            path.append(9)
            dfs(i+1,ra,rb-n[i]-1)
            path.pop()
    dfs(0,a,b)
    print(res)
    
if __name__=='__main__':
    solve()
```

用整数累积已经处理的数位

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    s,a,b=next(da),int(next(da)),int(next(da))
    def dfs(i,n,a,b):
        global res
        while i>=len(s):
            res=max(res,n)
            return
        x=int(s[i])
        d=min(9-x,a)
        dfs(i+1,n*10+(x+d),a-d,b)
        if b>=x+1:
            dfs(i+1,n*10+9,a,b-(x+1))
    dfs(0,0,a,b)
    print(res)
```

<a name="note-tsingpigdadademoban-531"></a>

### 记录方案与恢复现场

为什么可变路径要保存快照

> 带着 [1, 2] 进入下一层，立刻记录 [1, 2]。
> 只要是把一个“会随着时间变化的数据容器（列表、字典、集合）”塞进结果集里，
> 绝对、必须、永远要加上 .copy()！
> 否则你塞进去的，只是一个会随时爆炸的定时炸弹。

列表引用的实验

```python
path = [1]         # 第一步：我有一个列表，里面装了 1
ans = []           # 第二步：我有一个空的结果集
ans.append(path)   # 第三步：我把 path 塞进了 ans
path.append(2)     # 第四步：我往 path 里又加了一个 2

print(ans)         # 请问，现在打印 ans，结果是什么？
```

列表引用、递归返回与 pop 的原始笔记

> 按照人类的直觉，第三步塞进去的时候 path 是 [1]，所以最后 ans 应该是 [[1]]。
> 
> 但是！在 Python 里运行的结果是：[[1, 2]]
> 
> 为什么会发生这种“灵异事件”？
> 因为在 Python 中，像列表（List）这种可以不断变化的数据结构，
> 变量名其实只是一个“便利贴”（或者叫标签、指针），
> 它贴在了一块内存空间上。
> 
> 递归的本质，就是“看剧时的暂停键”。
> 当你在 dfs(0) 的循环里走到 dfs(1) 时，
> 相当于你把正在看的《第一季》按下了暂停，跑去把《第二季》从头到尾全看完了，
> 然后解除暂停，继续看《第一季》剩下的剧情。
> 
> 而那句看似没道理的 path.pop()，就是你每次看完后续剧情回来后，
> 必须把脑子里的杂念“清除”，才能继续看当下的剧情。

把路径用 join 存成字符串的例子

> 回想一下我们之前聊过的“连线”灾难：
> 如果你写的是 out.append(arr)，
> 那你就是往 out 里塞了一根指向 arr 这个木箱子的红线（内存引用）。
> 后续 arr.pop() 会把结果全毁掉。
> 
> 但是！请死死盯住你写的 join 操作到底干了什么：
> str(i) for i in arr：首先，它把篮子里的数字（比如 1 和 2），变成了字符 '1' 和 '2'。
> ' '.join(...)：然后，它用空格把这两个字符拼接起来，
> 在内存中凭空创造了一个全新的字符串对象："1 2"。
> out.append("1 2")：最后，你把这个崭新的字符串，放进了 out 数组里。
> 真相大白：
> 在这段代码里，你根本没有把 arr 这个列表塞进结果集里！你是在每一次触底的时候，利用 join 自动把 arr 里的内容“冲洗成了一张固定的实物照片（字符串）”，
> 然后把照片放进了相册 out 里！

何时把当前路径记入答案

> 当你以后在考场上面对一道回溯题，不知道 res.append 该写在哪里时，
> 你只需要问自己一个问题：
> 
> “我当前手里拿着的这个半截 path，题目认不认它是一个合法的答案？”
> 
> 如果认（比如求所有子集），那就一进函数，立刻拍照。
> 
> 如果不认（必须要固定长度，或者必须要全部选完），
> 那就憋着，带着它继续往下走，直到满足条件（走到最后）了，再拍照。

<a name="note-tsingpigdadademoban-558"></a>

### 组合枚举

固定选 k 个数，按每个数选或不选递归

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i):
            if len(path)==k:
                ans.append(path.copy())
                return
            if i>n:return#背包没满也要返回
            path.append(i)
            dfs(i+1)
            path.pop()
            dfs(i+1)
        dfs(1)
        return ans
```

洛谷 P1157。从 start 向后选数，避免产生重复组合

```python
##递归实现组合型枚举https://www.luogu.com.cn/problem/P1157
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n,r=int(next(da)),int(next(da))
##    通过引入 start 参数来限制每次 for 循环的起始位置，
##    强制序列单调递增，从而天然地消除重复组合并保证字典序。
##既然不回头，自然永远不会碰到之前用过的数字，也就不需要 visited 数组来防重了。    
    path=[]
    out=[]
    def dfs(st):
        if n - start + 1 < r - len(path):
            return
        if len(path)==r:
            out.append(''.join(f'{i:>3d}' for i in path))
            return
        for i in range(st,n+1):
            path.append(i)
            dfs(i+1)
            path.pop()
    dfs(1)
    sys.stdout.write('\n'.join(out)+'\n')                
if __name__=='__main__':
    solve()
```

<a name="note-tsingpigdadademoban-574"></a>

### 组合总和

排序后从当前下标继续选，允许重复使用候选数

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        ans=[]
        path=[]
        def dfs(i,s):
            if s==target:
                ans.append(path.copy())
                return
                #re
            for j in range(i,n):
                x=candidates[j]
                if x+s<=target:
                    path.append(x)
                    dfs(j,x+s)
                    path.pop()
                else:
                    break#
        dfs(0,0)
        return ans
```

<a name="note-dfs-39"></a>

### 子集枚举

指数型枚举。对照原稿中的递归树跟踪选与不选

```python
##指数型https://www.acwing.com/problem/content/94/
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    arr=[]
    out=[]
##这并非同时发生，而是顺序执行的“平行宇宙”：
##程序会先在选项A（不选）的分支里走到时间的尽头，
##然后再“时光倒流”（通过 return 回退到当前层），接着开启并探索选项B（选）的未来。
##                    root (state=[])
##                /                 \
##          (不选1)                   (选1, append(1))
##         dfs(2)                     dfs(2)
##        /      \                   /      \
##  (不选2)      (选2)         (不选2)       (选2)
##  dfs(3)       dfs(3)        dfs(3)        dfs(3)
##    |            |             |             |
## print([])    print([2])    print([1])   print([1, 2])
    def f(x):
        if x>n:

            out.append(' '.join(str(i) for i in arr))
            return
##        不选
        f(x+1)
        # 【核心逻辑】：一旦调用这个函数，当前这层代码就会被“冻结”。
    # 计算机在内存里保存了当前层走到了哪里，然后跳进 x+1 层去疯狂衍生。
    # 无论里面掀起多大波澜，只要它最终 return，就会解冻当前层，紧接着执行下一行。
        ##        选
        arr.append(x)
        f(x+1)
        arr.pop()

    f(1)
    sys.stdout.write('\n'.join(out)+'\n')
if __name__=='__main__':
    solve()
```

<a name="note-dfs-79"></a>

### 排列枚举

洛谷 P1706。用访问标记与路径生成排列

```python
####排列型https://www.luogu.com.cn/problem/P1706
##排列型
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    used=[False]*(n+1)
    arr=[]
    out=[]
##核心设计思想（一句话）：
##for 循环负责在“当前唯一的空位”上，横向枚举所有还没被用过的卡片；
##而 dfs() 负责纵向推进，把目光移动到“下一个空位”。    
    def dfs():
##        step2
        if len(arr)==n:
            out.append(''.join(f'{i:5d}' for i in arr))
            return
##        step1
        for i in range(1,n+1):
            if not used[i]:
                arr.append(i)
                used[i]=True
##dfs() 它连个参数都没有，怎么知道自己现在在第几层？怎么知道该排哪个格子？
##答案的核心只有四个字：全局变量（公共黑板）。               
                dfs()
                arr.pop()
                used[i]=False
    dfs()
    sys.stdout.write('\n'.join(out)+'\n')        
if __name__=='__main__':
    solve()
```

<a name="note-dfs-158"></a>

### 选数与素数和

关联知识点 · [素数判定与分解](#note-tsingpigdadademoban-80)

洛谷 P1036。读入 n、k，准备结果与路径

```python
####选数https://www.luogu.com.cn/problem/P1036
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n,k=int(next(da)),int(next(da))
    sz=[int(next(da)) for _ in range(n)]
    ans=0
    out=[]
    arr=[]
```

DFS 主干。到达 k 个数后按上面的素数表累计，保留 nonlocal 注解

```python
##    主干dfs
    def dfs(j):
        
##如果你没有用到函数嵌套（比如全局定义了 ans=0，然后直接并排定义了一个 def dfs():）：
##修改 ans 时，只能用 global。
##
##如果你用了函数嵌套（比如在 def solve(): 里面定义了 ans = 0，
##然后紧接着在它内部定义了 def dfs():）：修改 ans 时，必须用 nonlocal。
##
##在蓝桥杯 B 组 Python 的标准写法中，我们往往推荐把所有逻辑写在一个 def solve():里面
##（就像上一回合我给你纠错的代码一样）。
##这样不污染全局命名空间，因此 nonlocal 是 DFS 嵌套写法中的绝对主力。
        
        nonlocal ans# 【修复2】Python闭包修改外部不可变变量(int)时，
##        必须声明 nonlocal，否则会报 UnboundLocalError
        if len(arr)==k:
            su=sum(arr)
            if isp[su]:
                ans+=1
            return
        for i in range(j,n):
            arr.append(sz[i])
            dfs(i+1)
            arr.pop()
    dfs(0)
    print(ans)                
if __name__=='__main__':
    solve()
```

<a name="note-dfs-294"></a>

### 烤鸡的定长枚举

洛谷 P2089。十种配料的取值范围与方案总数

> 烤鸡https://www.luogu.com.cn/problem/P2089
> 这道题的本质是把一个数字n拆分成10个数字的和，且每个数字只能取1,2,3。
> 第一重识破（数学陷阱）：10种配料，每种最少1克，最多3克。
> 这意味着美味程度的总和最小是10，最大是30！
> 如果输入的n<10或者n>30，绝对不可能拼出来，直接输出0即可。
> 第二重识破（暴力极限）：既然有10个坑位，每个坑位有3种选择，
> 那么全宇宙的方案总数就是3^{10}=59049种。
> 区区不到6万种状态，连给计算机塞牙缝都不够，直接无脑枚举！

用 itertools.product 枚举十个位置

```python
##法一：itertools.product 是处理“定长、多选一”组合问题的绝对真神
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    from itertools import product
    if not 10<=n<=30:
        print(0)
    else:
        ans=[p for p in product(range(1,4),repeat=10) if sum(p)==n]
        print(len(ans))
        for p in ans:
            print(*p)
    
if __name__=='__main__':
    solve()
```

用 DFS 枚举，并按剩余坑位剪枝

```python
##法二
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
##    step2
    ans=0
    path=[]
    out=[]
    def dfs(ceng,he):
        nonlocal ans
        if (10-ceng)*3<n-he:return
        if 10-ceng>n-he:return
##        step4
##        if he==10:
        if ceng == 10:
            ans+=1
            out.append(' '.join(map(str,path)))
            return
##        step3
        for i in range(1,4):
            path.append(i)
            dfs(ceng+1,he+i)
            path.pop()
                    
##    step1
    if not 10<=n<=30:
        print(0)
    else:
        dfs(0,0)
        print(ans)
        if ans>0:
# 【细节优化】如果 ans 为 0（即没有合法方案），题目要求只输出一个 0，不能再输出空行
            sys.stdout.write('\n'.join(out)+'\n')    
if __name__=='__main__':
    solve()
```

<a name="note-dfs-356"></a>

### 火星人与字典序后继

洛谷 P1088。交换升序断点并反转后缀，逐次得到下一排列

```python
####火星人https://www.luogu.com.cn/problem/P1088
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n,m=int(next(da)),int(next(da))
    arr=[int(next(da)) for _ in range(n)]
##摒弃计算阶乘的全局视角，通过从右向左寻找首个升序对、交换并翻转后缀的局部贪心策略，
##以 O(N) 的代价步进 M 次推导出目标排列。
    for _ in range(m):
        i=n-2
        while not arr[i]<arr[i+1]:
            i-=1
        j=n-1
        while not arr[j]>arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        arr[i+1:]=reversed(arr[i+1:])#快过 [::-1](完整拷贝一次切片并
##        生成一个全新的列表，然后再赋给原列表，存在大内存申请开销)
    print(*arr)    
if __name__=='__main__':
    solve()
```

带讲解的 DFS，贴着目标排列确定起点

```python
##dfs版
import sys
sys.setrecursionlimit(20000)
def solve():
    da=iter(sys.stdin.read().split())
    n,m=int(next(da)),int(next(da))
    target=[0]+[int(next(da)) for _ in range(n)]#为了让 target 的索引也从 1 开始
##    （避免后续烧脑的 -1 偏移量），我们在最前面垫一个 0
##    step2
    visited=[False]*(n+1)##怎么知道数字 i 之前有没有被用过？需要引入 visited 数组
    path=[0]*(n+1)#填进去的数字存哪？需要引入 path 数组。
##    step4:完善终点与计数器
##    step4-part1:引入计数变量
    foundstart =False
    stepcount=0
##    step1
##    def dfs(depth):
##    step3:注入灵魂（推导贴边锁 is_edge）第一步怎么才能直接跳到火星人给的那个数字？
##    step3-part1:引入状态锁参数:我们必须给 DFS 加上一把锁
    def dfs(depth,isedge):
##    step4-part2:丰满递归终点
        nonlocal foundstart ,stepcount
        if depth==n+1:
##            return
            if not foundstart:
                foundstart=True# 第一次来，啥也不干，只把标记打上
            else:
                stepcount+=1
                if stepcount==m:
                    print(' '.join(map(str,path[1:])))
                    sys.exit(0)
##sys.exit(0) 的作用：
##它是 Python 提供给操作系统的“自毁指令”。
##只要代码摸到这一句，管你现在嵌套了多少层函数，管你外面还有多少个 for 循环没跑完，
##程序瞬间死亡（正常终止），直接把结果扔给评测机。
##这就是物理意义上的“拔掉主机电源”。                    
            return
                
##        for i in range(1,n+1):
##        step3-part2:改造循环的起点:如果被锁着，起点必须是 target[depth]；
##        如果自由了，起点才是 1
        start=target[depth] if isedge else 1
        for i in range(start,n+1):
##    step2
            if not visited[i]:
                visited[i]=True
                path[depth]=i

##                step3-part3:推导下一层的锁状态:
##        要进入下一层 dfs(depth + 1, ???)。传给下一层的参数是 True 还是 False 呢？
##        我们严密思考：只有当前是被锁着的（is_edge == True） 且
##        你乖乖听话选了目标数字（i == target[depth]） 时，
##        下一层才继续被锁。否则，立刻自由！
                nextisedge=isedge and (i==target[depth])
                
##                dfs(depth+1)
                dfs(depth+1,nextisedge)

                visited[i]=False
##            pass#pass是空语句(等待完善)，for后面必须有循环体，否则会报错；
##     所以用pass意思是：这里暂时什么都不做只是占一个位置，保证代码语法合法。
    dfs(1,True)   
if __name__=='__main__':
    solve()
```

纠错笔记，重点检查贴边状态、递归终点和 visited 的恢复时机

```python
##纯享dfs:1
import sys
sys.setrecursionlimit(20000)
def solve():
    da=iter(sys.stdin.read().split())
    n,m=int(next(da)),int(next(da))
    target=[0]+[int(next(da)) for _ in range(n)]
    path=[0]*(n+1)
    visited=[False]*(n+1)
##  isedge=False：不要放在这，况且一开始得默认是True，才能看后面打不打破，直接传参
    foundstart=False
    stepcount=0
    def dfs(depth,isedge):
        nonlocal foundstart,stepcount# 【修复1：声明写权限】
##        if depth == n:
        if depth == n+1:# 【修复2：终点必须是越界的 n + 1】
            #已修：注意depth等于几代表准备填第几个坑；depth=n+1代表填完n个
        
            if not foundstart:
                foundstart=True
            else:
                stepcount+=1
                if stepcount==m:
                    print(' '.join(map(str,path[1:])))
##                    exit(0)# 建议加上 sys.
                    sys.exit(0)
            return
##        if path[depth]==target[depth]:
##            isedge=True
##逻辑谬误： 你在这个时候，连 for 循环都还没进去，
##当前的坑位 path[depth] 里面还是个 0！你拿一个还没填入的空坑，去跟 target 比较，
##        这是典型的“用未来的果，倒推现在的因”。
##而且，isedge 是上一层传给你的既定事实，你绝对不能在这一层的开头强行篡改它。
##理顺意识： 当前层的 isedge 是历史的遗产，直接用它来决定 start 就行了。
##至于“下一步还不贴边”，那是你做出选择之后才能推算的事情！
        
##        start=target[depth] if isedge==True else 1# 【修复3：删除时序错乱的判断，
##        直接使用祖先传下来的 isedge 决定起点】
        start=target[depth] if isedge else 1
        for i in range(start,n+1):
            if not visited[i]:
                visited[i]=True
                path[depth]=i
##                nextisedge=True if path[depth]==target[depth] else False
##逻辑谬误： 假设火星人的目标是 [3, 1, 2]。
##你在第一坑填了 4，锁被打破了，传给第二坑的 isedge = False。
##你在第二坑获得了自由，于是你顺手挑了一个极小值 1。
##但根据你这句代码，它发现 path[2] (也就是1) == target[2]！
##于是它强行把 nextisedge 变成了 True！
##本来已经自由的时间线，竟然因为一次巧合，又被重新戴上了镣铐！
##理顺意识： 自由是不可逆的！下一层继续被锁的唯一充分必要条件是：
##上一层传给我的锁还在（isedge 为真） AND 我这一步乖乖走了原路（i == target[depth]）。
                nextisedge=isedge and (i==target[depth])#已修
                dfs(depth+1,nextisedge)
                visited[i]=False#已修
##            visited[i]=False
##visited 数组：这是图书馆的借书登记系统。
##visited[i] = True 表示第 $i$ 本书被借走了，False 表示书还在架子上。
##if not visited[i]:：这是图书管理员的结界（门禁）。
##只有当书在架子上时，才允许你走进去执行后续动作。
##visited[i] = True：你把书借走。
##visited[i] = False：你把书还回去。
##for i in range(1, 4):
##    if not visited[i]:         # 管理员：书在吗？
##        visited[i] = True      # 你：在，我借走了！
##        dfs(depth + 1)         # 你：拿着书走向下一层...
##        
##    visited[i] = False         # ⚠️ 致命错误：这行代码在结界外面！
##物理矛盾： 第 2 层的你，明明连门都没进，连书都没碰到，
##却在系统里强行登记了一笔：“书 1 已经归还”！                

##            path[depth]=0(这句其实可以省略，因为下次填入会直接覆盖)
    dfs(1,True)
    
if __name__=='__main__':
    solve()
```

精简 DFS，保留注释掉的输入样例

```python
import sys
sys.setrecursionlimit(20000)
def solve():
    da=iter(sys.stdin.read().split())
##    da=iter('''5
##3
##1 2 3 4 5
##'''.split())
    
    n,m=int(next(da)),int(next(da))
    target=[0]+[int(next(da)) for _ in range(n)]
    visited=[False]*(n+1)
    path=[0]*(n+1)
    foundstart=False
    stepcount=0
    def dfs(depth,isedge):
        nonlocal foundstart,stepcount
        if depth==n+1:
            if not foundstart :
                foundstart=True
            else:
                stepcount+=1
                if stepcount==m:
                    print(' '.join(map(str,path[1:])))
                    sys.exit(0)
            return
        start=target[depth] if isedge else 1
        for i in range(start,n+1):
            if not visited[i]:
                visited[i]=True
                path[depth]=i
                nextisedge=isedge and(i==target[depth])
                dfs(depth+1,nextisedge)
                visited[i]=False
    dfs(1,True)
if __name__=='__main__':
    solve()
```

<a name="note-dfs-561"></a>

### 火柴加法

洛谷 P1149。预计算数字的火柴数，枚举加数并检查等式

```python
##火柴加法https://www.luogu.com.cn/problem/P1149
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    if n<=4:
        print('0')
        return
    path=[0]*2
    ans=0
    num=[0]*2005#num[c]
##    num=[0]*1000
    num[0]=6#
    m=[6,2,5,5,4,5,6,3,7,6]
##    for i in range(2005):
    for i in range(1,2005):
        t=i
        c=0
        while t>0:
            c+=m[t%10]
            t//=10
        num[i]=c
            
##        num[i]=m[i%10]+m[i//10%10]+m[i//100%10]+m[i//1000]  有前导0问题
        
    def dfs(depth,used):
        nonlocal ans
        if used>n-4:
            return
        
        if depth==2:
            c=path[0]+path[1]
            if num[c]==n-used-4:
                ans+=1
##            return#校验失败： 此时程序进行校验 if num[c] == n - used - 4:。
##绝大多数情况下，随便凑出来的两个数 $A$ 和 $B$ 是不等于规定火柴数的。
##所以这个 if 语句不成立。
            return#必须和if平级
            
        for i in range(1000):
            path[depth]=i
            dfs(depth+1,used+num[i])
    dfs(0,0)
    print(ans)         
            
if __name__=='__main__':
    solve()
```

<a name="note-dfs-610"></a>

### 配料的酸度与苦度

关联知识点 · [按位枚举配料子集](#note-dfs-722)

带 haschosen、参数与作用域讨论的调试草稿，保留报错写法

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    s=[0]+[0]*n
    b=[0]+[0]*n
    for i in range(1,n+1):#不能用_循环
        s[i],b[i]=int(next(da)),int(next(da))
    minans=float('inf')
    def dfs(i,suan,ku,haschosen):
        nonlocal minans
        【剪枝前置的贪心更新】
        if haschosen:
            minans=min(minans,abs(suan-ku))

        for nexti in range(i,n+1):#不用path，for从i开始循环顶级自然去重不用路径
            #这个非常核心！！！！！！！！！！！！！！！！！
            dfs(nexti+1,suan*s[nexti],ku+b[nexti],True)
    dfs(1,1,0)#【启动修复】：因为配料是从 1 开始的，所以起始游标 i 必须是 1
            
    path=[0]+[0]*(n+1)
    suan=0
    ku=0
    def dfs(depth,suan,ku,path):
        nonlocal minans,suan,ku
    # 💥 致命漏洞 2：参数与 nonlocal 的作用域冲突
    # 你把 suan 和 ku 既当成了函数参数，又在内部声明为 nonlocal。
    # Python 语法严禁此操作，直接抛出 SyntaxError 阻止运行。
        deff = abs(suan-ku)
    # 💥 致命漏洞 3：时序错位
        # 在第 0 层刚进来，什么都没选，你就开始算差值了。此时初始值是错的。
        if depth==n+1 and sum(path):
            minans=min(minans,deff)
        # 💥 致命漏洞 4：缩进刺客引发的逻辑截断
        # 你的 return 与 if 平级！这意味着哪怕 depth=0，
        # 函数走到这里就直接 return 了！后面的搜索代码 100% 无法执行。
        return

        path[depth]=1
        if sum(path):
            suan*=s[depth]
        else:
            suan+=s[depth]
        ku+=b[depth]
        dfs(depth+1,suan,ku)
##启示（状态的无损传递）：
##最高级的回溯，是不修改当前状态，而是将“计算后的新状态”直接作为参数传给下一层。
##例如：dfs(depth + 1, suan * s[depth])。下一层返回时，
##当前层的 suan 根本没变，完全不需要写恶心的 //=  逆运算。        
        if sum(path)==1:
            suan-=s[depth]
        else:
            suan//=s[depth]
        避坑指南（数学系特供）：不要用逆运算去回溯！
你试图用 suan //= s[depth] 去撤销 suan *= s[depth]。
虽然数学上 $A \times B \div B = A$，但在编程中这是一种极其脆弱的“破坏性回溯”。
一旦涉及初始值 0、浮点精度或负数取整，必定崩盘。
            
        ku-=b[depth]
        path[depth]=0
        dfs(depth+1,suan,ku)
    dfs(0,0,0,path)
    print(minans)        
if __name__=='__main__':
    solve()
```

用路径标记选取哪些配料，叶节点计算酸苦差

```python
import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    n = data[0]
    s = [data[i] for i in range(1, len(data), 2)]
    b = [data[i] for i in range(2, len(data), 2)]
    
    ans = float('inf')
    path = [0] * n  # 0表示不选，1表示选
    
    def dfs(depth):
        nonlocal ans
        if depth == n:
            # 只有当 path 里有 1（至少选了一个）时才计算
            if sum(path) > 0:
                cur_s = 1
                cur_b = 0
                for i in range(n):
                    if path[i] == 1:
                        cur_s *= s[i]
                        cur_b += b[i]
                ans = min(ans, abs(cur_s - cur_b))
            return
            
        # 尝试不选
        path[depth] = 0
        dfs(depth + 1)
        
        # 尝试选
        path[depth] = 1
        dfs(depth + 1)
        
        # 其实可以不用显式恢复 path[depth]=0，因为上层会被覆盖
        # 但写上是标准回溯的美学
        path[depth] = 0 

    dfs(0)
    print(ans)

solve()
```

<a name="knowledge-enum"></a>

### 递归分支与终止条件

逐个位置探索可行选择的 DFS 骨架

```python
ans=初始答案
def dfs(i,其他状态):
    global ans
    #1.终止条件：所有位置处理完，返回上一层
    if i==总长度：
        当前结果更新 ans
        return
    #2.取出当前位置信息
    cur=当前对象
    #3.枚举当前位置可行选择
    if 选择1可行：
        dfs(i+1,选择1后的状态)
    if 选择2可行：
        dfs(i+1,选择2后的状态)
    ...
dfs(起点状态)
print(ans)
```

<a name="topic-bfs"></a>

## BFS 与最短步数

网格扩散与开关谜题共用按层扩展的写法，队列分别存坐标和灯光状态。

- [网格上的多源 BFS](#note-tsingpigdadademoban-595)
- [开关谜题的状态空间 BFS](#note-tsingpigdadademoban-705)
- [网格连通块与最大面积](#knowledge-area)

<a name="note-tsingpigdadademoban-595"></a>

### 网格上的多源 BFS

起点、分层、入队标记与边界检查

> 二、 遇到 BFS，脑子里必须过电的 4 个考量要素
> 以后只要题目里出现“最短路径”、“最少步数”、“层层扩散”、
> “几天后蔓延到全图”这种字眼，立刻条件反射呼叫 BFS。
> 动手写代码前，必须拷问自己这 4 个问题：
> 1.起点是“单源”还是“多源”？
>     只有一个起点（走迷宫）：开局入队一个坐标。
>     有多个起点（病毒扩散、森林火灾）：开局遍历全图，把所有起点全部扔进队列！
> 2.需要“分层（时间概念）”吗？
>     如果题目问“能不能走到终点”，不需要分层，直接 while q:
>         无脑拿出来扩散就行。
>     如果题目问“第 k 天的状态”或“最少走几步”，必须严格分层，
>         必须加上 for _ in range(len(q)):，
>         并且在 for 循环外面加上步数/天数递增（你的代码里是 k -= 1）。
> 3.有没有严格的“入队即标记（判重）”？
>     绝对不能让同一个节点被重复扔进队列。
>     必须用一个 visited 集合，
>     或者像你这样直接修改原数组 g[nx][ny] = 1 来充当防重墙。
> 4.越界与合法性检查是否前置？
>     永远在“准备往队列里塞”的时刻（nx, ny），
>     立刻检查是否越过了长宽边界，是否是墙壁。        

长草初稿。源点坐标、边界判断和输出括号都有待修处

```python
import sys
from collections import deque
def solve():
    da=iter(sys.stdin.read().split())
    n,k=int(next(da)),int(next(da))
    grid=[list(0 if x=='.' else 1 for x in next(da)) for _ in range(n)]
    q=deque()
    di=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(n):
        for j in range(m):
            if grid[x][y]==1:
                q.append((x,y))
    def bfs():
        nonlocal k
        while q and k:
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in di:
                    nx,ny=x+dx,y+dy
                    if grid[nx][ny]==0 and 0<=nx<n and 0<=ny<y:
                        grid[nx][ny]=1
                        q.append((nx,ny))
            k-=1
    bfs()
    out=[]
    for x in range(n):
        row=['.' if grid[x][y]==0 else 'g'  for y in range(m))]
        out.append(''.join(row))
    sys.stdout.write('\n'.join(out)+'\n')
    
if __name__=='__main__':
    solve()
```

长草修订版。收集所有初始草格，同时扩展 k 层

```python
import sys
from collections import deque

def solve():
    # 1. 初始化迭代器
    da = iter(sys.stdin.read().split())
    try:
        n = int(next(da))
        m = int(next(da)) # 修复 1：读取 m
    except StopIteration:
        return
        
    # 2. 读取网格
    grid = [[0 if x == '.' else 1 for x in next(da)] for _ in range(n)]
    
    # 3. 读取天数 k
    k = int(next(da))
    
    q = deque()
    di = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # 4. 收集源点 (修复 2：变量名 i, j)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j))
                
    def bfs():
        nonlocal k
        while q and k > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in di:
                    nx, ny = x + dx, y + dy
                    # 修复 3：边界判定必须放在前面！且列的边界是 m
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            k -= 1
            
    bfs()
    
    # 5. 输出结果 (修复 4：去掉了多余的括号)
    out = []
    for i in range(n):
        row = ['.' if grid[i][j] == 0 else 'g' for j in range(m)]
        out.append(''.join(row))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
```

长草练习中的建图、扩散与输出草稿

```python
import sys
from collections import deque
def solve():
    da=iter(sys.stdin.read().split())
    di=[(1,0),(-1,0),(0,1),(0,-1)]
    n,m=int(next(da)),int(next(da))
    q=deque()
    g=[[0]*n for _ in range(m)]‘
    rows=[list(next(da)) for _ in range(n)]
    for i  in range(n):
        for j in range(m):
            if rows[i][j]=='g':
                g[i][j]=1
                q.append((i,j))
    ans=0
    k=int(next(da))
    while q and k:
        x,y=q.popleft()
        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and g[nx][ny]==0:
                g[nx][ny]=1
                q.append((nx,ny))
        k-=1
    for row in g:
        ans=''.join('g' if x else '.' for x in row)     ''.join必须放可迭代对象       
```

<a name="note-tsingpigdadademoban-705"></a>

### 开关谜题的状态空间 BFS

关联知识点 · [用整数表示集合](#note-tsingpigdadademoban-1002)

用异或产生下一状态，入队前判重

```python
for mask in unique_effects:
    next_state = curr_state ^ mask
    if next_state not in visited:
        visited.add(next_state)
        q.append(next_state)
```

逐行推演开关动作与异或结果

> 第一句：for mask in unique_effects:
> 物理映射：你面前的桌子上，
> 摆着你在第一步预处理时提炼出来的所有“不重复的魔法面具（开关操作）”。
> 这行代码的意思是：“我要把桌子上的每一个按钮，全都试按一遍。”
> 
> 深度逻辑：在走迷宫时，这一步相当于 for dx, dy in 方向数组
> （尝试上下左右四个方向）。而在状态空间里，你的“方向”就是这些面具。
> 每一个 mask，代表着向一个全新的灯光状态迈进的可能。
> 
> 第二句：next_state = curr_state ^ mask
> 物理映射：按下按钮，见证奇迹！
> 
> 深度逻辑：这是最绝妙的一行位运算代码。^ 是异或符号，
> 它的铁律是：相同为 0，不同为 1。
> 
> 假设你摸到了一个 mask = 2（二进制 00010，代表翻转灯 1）。
> 
> 现在的房间 curr_state 是 00110。
> 
> 发生异或碰撞：
> 00110 (当前房间)
> 00010 (魔法面具)
> ------- (异或)
> 00100 (新房间 next_state)
> 
> 结果：原本亮着的灯 1（第 1 位）被面具里的 1 给“异或”成了 0（灭了）；
> 原本亮着的灯 2（第 2 位）碰到了面具里的 0，
> 保留了 1（继续亮着）。这行代码瞬间完成了多个灯泡的同时翻转，
> 并计算出了按完之后的新格局 next_state。
> 
> 第三句：if next_state not in visited:
> 物理映射：查验生死簿，防止死循环。
> 
> 深度逻辑：按完开关，房间变成了 next_state。
> 这时候你必须立刻停下来，翻开你手里的 visited 集合，
> 问自己一个问题：“这种灯光亮暗的组合，我以前是不是曾经踩出来过？”
> 
> 如果你在第 1 层就踩出过 00100，现在你到了第 5 层，
> 一顿操作后又搞出了 00100。
> 
> 这说明你刚才的操作纯属绕远路（脱裤子放屁）！
> 别人按 1 次就能达到的状态，你按了 5 次才达到，这绝对不可能是“最短路径”。
> 
> 只有当 next_state not in visited 成立
> （这是一种全宇宙首次发现的全新灯光格局），你才被允许进入下一步。

原稿对照表：网格上的坐标与灯光的位掩码

> 概念            长草问题（物理网格 BFS）	开关谜题（状态空间 BFS）	         它的物理意义是什么？
> 当前位置        x, y = q.popleft()	curr_state = q.popleft()	我现在站在哪里？（现在的局面是什么）
>                   
> 尝试动作        for dx, dy in di:	for mask in unique_effects:	我下一步可以往哪走？（我可以按哪个开关）
> 
> 产生变化        nx = x + dx             next_state = curr_state ^ mask  执行动作后，到达的新地点 / 产生的新局面
>                 ny = y + dy
> 
> 防止回头        if grid[nx][ny] == 0:	if next_state not in visited:	这个新地点/新局面，我以前来过吗？
> 
> 登记入队        grid[nx][ny] = 1        visited.add(next_state)         没来过！赶紧打上标记，塞进队列明天处理
>                 q.append((nx, ny))      q.append(next_state)

完整讲解版，按层搜索最少按键次数

```python
import sys
from collections import deque

def solve():
    # 使用快读
    da = iter(sys.stdin.read().split())
    try:
        t = int(next(da))
    except StopIteration:
        return
        
    out = []
    for _ in range(t):
        n = int(next(da))
        m = int(next(da))
        
        # 1. 预处理：提取所有【本质独特】的开关面具
        unique_effects = set()
        for r in range(min(n, m)):
            lamp1 = r
            lamp2 = (2 * r) % m
            
            effect_mask = 1 << lamp1
            if lamp1 != lamp2:
                effect_mask ^= (1 << lamp2)
                
            unique_effects.add(effect_mask)
            
        goal_state = (1 << m) - 1
        
        # 2. 核心：将 BFS 逻辑完美打包成独立函数
        def bfs():
            # 队列和记忆化集合放在函数内部，确保每次调用都是干净的
            q = deque([0])
            visited = {0} 
            step = 0
            
            while q:
                # 锁定当前层的快照长度
                for _ in range(len(q)):
                    curr_state = q.popleft()
                    
                    # 【神级优化】：一旦触底，直接 return 答案！
                    # 彻底消灭了 found 变量和两层 break！
                    if curr_state == goal_state:
                        return step
                        
                    for mask in unique_effects:
                        next_state = curr_state ^ mask
                        if next_state not in visited:
                            visited.add(next_state)
                            q.append(next_state)
                            
                step += 1 # 这一层（按键次数）探索完毕，步数加 1
                
            # 如果 while 循环自然结束（队列空了），说明无解
            return -1
            
        # 3. 直接调用函数，接收结果并转成字符串存入 out
        ans = bfs()
        out.append(str(ans))
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
```

再写一遍。保留 op 的缩进与重复灯位的纠错记录

```python
import sys
from collections import deque
def solve():
    da=iter(sys.stdin.read().split())
    t=int(next(da))
    out=[]
    for _ in range(t):
        n,m=int(next(da)),int(next(da))
##        move=[]
        move=set()
        for i in range(min(n,m)):
            lamp1=i
            lamp2=(2*i)%m
##            mv=1<<lamp1
##            if lamp1 != lamp2:
##                mvm=1<<lamp2
##                op=mv^mvm
##“你让我把 op 加进集合里，可是如果你不进 if，这个 op 根本就没被创建出来啊！
##            move.add(op)#缩进
            op=1<<lamp1
            if lamp1 != lamp2:
                op^=(1<<lamp2)
            move.add(op)           
        def bfs():
            q=deque([0])#状态待处理
            visited={0}#状态一出戏那
            step=0
            while q:
                for _ in range(len(q)):
                    cur_st=q.popleft()
                    if cur_st==(1<<m)-1:return step
                    for op in move:
                        new_st=cur_st^op
                        if new_st not in visited:
                            visited.add(new_st)
                            q.append(new_st)
                step+=1
            return -1
        out.append(str(bfs()))
    sys.stdout.write('\n'.join(out)+'\n')  
        
if __name__=='__main__':
    solve()
```

用 visited 与 cost 数组记录灯光状态及最少步数

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
##    da=iter('''2
##4 4
##5 5'''.split())
    
    t=int(next(da))
    def bfs(n,m):
        visited=[False]*(1<<m)
        cost=[float('inf')]*(1<<m)
        cost[0]=0
        from collections import deque
        q=deque([0])
        while q:
            state=q.popleft()
##            if cost[(1<<m)-1]!=float('inf'):
##                break
            for i in range(n):
                d1=i%m
                d2=2*i%m
                if d1==d2:
                    newstate=state^(1<<d1)
                else:
                    newstate=state^(1<<d1)
                    newstate=newstate^(1<<d2)
                if not visited[newstate]:
                    visited[newstate]=True
##                    q.append(newstate)
                    cost[newstate]=cost[state]+1
                    if newstate==(1<<m)-1:#
                        print(cost[(1<<m)-1])#
                        return # 找到答案，直接拔掉这台 BFS 机器的电源，让外面的 for 循环继续开下一局！
                    q.append(newstate)#
        print('-1')        
##        print(cost[(1<<m)-1]) if not cost[(1<<m)-1]==float('inf') else print('-1')
    for _ in range(t):
##        n,m=int(next(da)),int(next(da))
##        bfs(n,m)
        bfs(int(next(da)),int(next(da)))#
        
if __name__=='__main__':
    solve()
```

<a name="knowledge-area"></a>

### 网格连通块与最大面积

四邻域搜索，统计每个连通块的面积

```python
def solve(g):
    n,m=len(g),len(g[0])
    res=0
    di=[(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(i,j):
        ans=1
        g[i][j]=0
        q=deque([(i,j)])
        while q:
            x,y=q.popleft()
            for dx,dy in di:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and g[nx][ny]:
                    q.append((nx,ny))
                    ans+=1
                    g[nx][ny]=0
        return ans                    
    for i, row in enumerate(g):
        for j,x in enumerate(row):
            if x==1:
                res=max(bfs(i,j),res)
    return res                
```

<a name="topic-graph"></a>

## 图的表示与遍历

对照矩阵和邻接表存边的方式，再看沿后继搜索时如何记录访问深度。

- [沿后继搜索环](#note-tsingpigdadademoban-509)
- [带权无向图与 DFS](#note-tsingpigdadademoban-1027)

<a name="note-tsingpigdadademoban-509"></a>

### 沿后继搜索环

用字典记录访问深度的尝试。多个起点共用记录，跨轮次的深度差需要复核

```python
import sys
sys.setrecursionlimit(10000)
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
    arr=[0]+[int(next(da)) for _ in range(n)]
    zd={}
    res=0
    def dfs(i,idx):
        nonlocal res
        if zd.get(i) is not None:
            res=max(res,idx-zd[i])
            return
        zd[i]=idx
        dfs(arr[i],idx+1)        
    for i in range(1,n+1):
        dfs(i,1)
    print(res)
if __name__=='__main__':
    solve()
```

用当前递归路径识别环的伪代码

```python
def dfs(u,d):
    标记当前节点正在路径中
    v=下一步
    if v 没访问过：
        dfs(v)
    elif v 在当前路径：
        找到环，更新答案
    标记当前点处理完成
```

用路径深度差计算环长的草稿

```python
import sys
def solve():
    da=iter(sys.stdin.read().split())
    sys.setrecursionlimit=10**5
    n=int(next(da))
    g=[0]+[int(next(da)) for _ in range(n)]
    state=[0]*(n+1)
    res=0
    def dfs(i,idx,d):
        global ans
        if i in d:
            ans=max(ans,idx-d[i])
            return
        if state[i]:
            return
        d[i]=idx
        state[i]=1
        dfs(g[u],idx+1,d)
    for i in range(1,n+1):
        if not state[i]:
            d={}
            dfs(i,1,d)
```

<a name="note-tsingpigdadademoban-1027"></a>

### 带权无向图与 DFS

邻接矩阵、邻接表与遍历草稿。矩阵行初始化、DFS 形参与边的拆包顺序待核对

```python
g=[float('inf')*n for _ in range(n)]
u,v,w
g[u][v]=g[v][u]=w
g[u][u]=g[v][v]=0

e=[[] for _ in range(n)]
u,v,w
e[u].append((v,w))
e[v].append((u,w))

s=set()
def dfs(st):
    print(u,end=' ')
    s.add(u)
    for _ ,v in e[u]:
        if v not in s:
            dfs(v)
            s.add(v)
```

<a name="topic-bits"></a>

## 位运算与子集

让每一位表示是否选中一个元素，用掩码查询、修改或枚举整个集合。

- [用整数表示集合](#note-tsingpigdadademoban-1002)
- [按位枚举配料子集](#note-dfs-722)
- [二进制取位与奇偶判断](#knowledge-bits)

<a name="note-tsingpigdadademoban-1002"></a>

### 用整数表示集合

查位、置位、清位、判空、判满与翻转的六条速记

> 技巧 1：查看第 j 个物品有没有被用过
> 代码：if (S >> j) & 1 == 1:
>     理解：把 S 的第 j 位推到最右边，然后和 1 进行“按位与”（&）。
>     如果结果是 1，说明用过了。
> 
> 技巧 2：把第 j 个物品标记为已用（本题讲解）
> 代码：S = S | (1 << j)理解：强行把第 j 位置为 1。
> 
> 技巧 3：把第 j 个物品恢复为未用（回溯时常用）
> 代码：S = S & ~(1 << j)
> 理解：~ 是按位取反。制造一个“唯独第 j 位是 0，其他全是 1”的掩码，
> 用“按位与”把第 j 位强行清零。
> 
> 技巧 4：判断是不是一个物品都没用过
> 代码：if S == 0:
> 
> 技巧 5：判断是不是所有 $N$ 个物品全用完了
> 代码：if S == (1 << n) - 1:
> 理解：比如 $N=3$，1<<3 是 8（二进制 1000），
> 减去 1 就是 7（二进制 0111），恰好是前 3 位全为 1。
>                              
> 技巧 6：改变状态
> 代码：S^(1<<j)

<a name="note-dfs-722"></a>

### 按位枚举配料子集

关联知识点 · [配料的酸度与苦度](#note-dfs-610)

从非空子集到整数掩码的原始笔记

> 对于数学系学生来说，集合的子集和二进制数构成了完美的双射（Bijection）。
> $n$ 个物品的选与不选，完美对应 $0 \sim 2^n - 1$ 的每一个整数的二进制位。
> 这彻底消灭了函数调用的开销，速度提升极限！

逐位累计酸度积与苦度和，和同题的 DFS 写法对读

```python
import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    s = [int(data[i]) for i in range(1, len(data), 2)]
    b = [int(data[i]) for i in range(2, len(data), 2)]
    
    ans = float('inf')
    
    # 1 << n 相当于 2 的 n 次方。例如 n=3，范围是 1 到 7 (即二进制 001 到 111)
    # 从 1 开始，天然排除了 000 (什么都不选) 的非法情况
    for mask in range(1, 1 << n):
        cur_s = 1
        cur_b = 0
        
        # 检查这个整数的每一位
        for i in range(n):
            # 位运算：(1 << i) 是制作一个掩码，& 操作判断第 i 位是否为 1
            if mask & (1 << i):
                cur_s *= s[i]
                cur_b += b[i]
                
        ans = min(ans, abs(cur_s - cur_b))
        
    print(ans)

solve()
```

<a name="knowledge-bits"></a>

### 二进制取位与奇偶判断

用按位与判断奇偶，并用右移读取第 k 位

> 天下第一快的奇偶判断：
> 判断一个数是奇数还是偶数，初学者都写 if n % 2 == 0:。
> 奇数的二进制最后一位永远是 1，偶数的最后一位永远是 0。
> 所以，真正的高手判断奇偶性，
> 永远写 if n & 1: （说明是奇数）或者 if not (n & 1):（说明是偶数）。
> 
> 3. 联合终极公式：(n >> k) & 1
> 功能： 这是计算机底层源码中最常见的公式，用于**“获取数字 $n$ 的第 $k$ 个二进制位的值”**。对比：
> 它和十进制的 (n // (10 ** k)) % 10 在逻辑上完全对称，但在执行速度上快了无数倍。
> & 1 等价于 % 2

<a name="topic-math"></a>

## 数论与素数筛

从单次试除到批量筛选，再用前缀和做区间查询、用最小质因子表做分解。

- [筛法与区间计数](#note-tsingpigdadademoban-50)
- [素数判定与分解](#note-tsingpigdadademoban-80)
- [整数拆位与数位和](#knowledge-digits)
- [整数平方根](#knowledge-sqrt)
- [坐标距离与三角形面积](#knowledge-geo)
- [交错和与调和和](#knowledge-series)
- [数位出现次数](#knowledge-countdig)
- [模幂运算](#knowledge-pow)
- [拼接整数序列的第 n 位](#knowledge-digitstr)

<a name="note-tsingpigdadademoban-50"></a>

### 筛法与区间计数

先标记合数，再通过前缀和回答闭区间内的合数个数

```python
import sys
import math
def solve():
    
    n=10**7
    ip=[False]*(10**7+1)
    ip[0]=ip[1]=False
    for i in range(2,math.isqrt(n)+1):
        if  not ip[i]:
            for j in range(i**2,n+1,i):
                ip[j]=True
    qz=[0]*(n+1)
    for i in range(0,n):
        qz[i+1]=qz[i]+ip[i+1]
    out=[]
    data=sys.stdin.read().split()
    da=iter(data)
    for _ in range(len(data)//2):
        a,b=int(next(da)),int(next(da))
        ans=qz[b]-qz[a-1]
        out.append(str(ans))
    sys.stdout.write('\n'.join(out)+'\n')
    
if __name__=='__main__':
    solve()    
```

<a name="note-tsingpigdadademoban-80"></a>

### 素数判定与分解

关联知识点 · [选数与素数和](#note-dfs-158)

用奇数试除到整数平方根，调用前需要导入 isqrt

```python
def ip(n):
    if n==2 or n==3:return True
    if n&1!=1 or n<2:return False
    for i in range(3,isqrt(n)+1,2):
        if n%i==0:return False
    return True#老是忘记
```

选数题的三种判定需求与选型笔记

```python
##在考场上看到素数，按这个顺序在脑子里过一遍：
##
##题目只要我判断几个人是不是素数？
##👉 无脑写试除法。 （省内存，代码只有5行）
##
##题目要我求出 1 到 100 万范围内所有的素数？
##👉 无脑写 bytearray + 切片埃氏筛。 （Python 的极限跑分王）
##
##题目不仅要求素数，还让我疯狂给数字做“质因数分解”？每一个合数的“最小质因子”是什么。
##👉 被迫掏出欧拉线性筛。 （利用它的最小质因子特性）  
```

朴素埃氏筛。这里的 isp 表供选数题的 DFS 主干查询

```python
##法一：挨氏筛MLE    
    import math
    isp=[True]*(sum(sz)+1)
    isp[0]=isp[1]=False
    for i in range(2,math.isqrt(sum(sz))+1):
        if isp[i]:
            for j in range(i**2,sum(sz)+1,i):
                isp[j]=False
```

试除法。排除小于 2 的数与偶数，再枚举奇因子

```python
##法二：试除法
    def isprime(n):
        if n==2 or n==3:return True
        if n<2 or not n&1:return False
        for i in range(3,math.isqrt(n)+1,2):
            if n%i ==0:
                return False
        return True
```

用 bytearray 做切片埃氏筛，推导替换的字节数

```python
##法三极速挨氏筛（实际比欧拉晒快）
    def jsaishishai(n):
##切片长度公式：长度 = (终点 - 起点) // 步长 + 1
##即：length = (n - i * i) // i + 1
        isprime=bytearray([1])*(n+1)# 生成包含 n+1个 1 的字节数组
##bytearray它是 malloc 的化身
##1. 传入单独的整数：代表“开辟空地”;如果你写 bytearray(10)
##代表开辟 10 个字节的连续内存！因为是刚开辟的，所以默认全部填 0。
##2. 传入一个可迭代对象（如列表）：代表“填入数据”
##如果你写 bytearray([1])，它是把列表里的元素“翻译”成字节。
        isprime[0]=isprime[1]=0
        for i in range(2,math.isqrt(n)+1):
            if isprime[i]:
                length=(n-i*i)//i+1
                isprime[i*i:n+1:i]=bytearray([0])*length
##步长切片赋值 (is_prime[start : stop : step] = bytearray(...))
##功能： Python 高阶切片语法。
##将右侧的可迭代对象中的值，按顺序依次填入左侧按步长选出的坑位中。
##语法规则铁律： 当使用带有步长（step）的切片进行赋值时，
##等号右边的长度必须与左侧被选中的坑位数量绝对相等，
##多一个少一个都会报 ValueError。                
        return [i for i,prime in enumerate(isprime) if prime]
```

切片筛重写草稿。第 224 行把切片的冒号写成了逗号

```python
## prime 是我们在这行代码里“现场起的名字”，它来源于 enumerate 吐出来的数据！
    def jsaishishai(n):
        isprime=bytearray([1])*(n+1)
        isprime[0]=isprime[1]=0
        for i in range(2,math.isqrt(n)+1):
            if isprime[i]:#######
                length=(n-i*i)//i+1
                isprime[i*i,n+1,i]=bytearray([0])*length
        return [i for i,prime in enumerate(isprime) if prime]
```

欧拉筛与最小质因子表草稿。第 237 行判定要核对 spf 和 isp

```python
##法四：欧式筛(此版本即可马上筛查一个数是不是素数、如果是合数其最小质因子、所有素数)
##在外层枚举数字 i 的同时，内层枚举已知的质数 p，划掉它们的乘积 i * p；
##一旦发现 i 已经是 p 的倍数，立刻停止内层枚举，从而保证所有合数只被其最小质因子处理。    
    def eulerwithspf(n):
        spf=list(range(n+1))
        isprime=[True]*(n+1)
        isprime[0]=isprime[1]=False
        prime=[]
        for i in range(2,n+1):
            
            if isp[i]==i:
                # 即if is_prime[i]:如果 i没被划掉，那它一定是质数，收编进prime数组
                prime.append(i)
                
            for p in prime:
                if i*p>n:# 越界保护：如果乘积已经超过了我们要找的范围 n，直接跳出
                    break
                
                # 划掉合数：用最小质因子 p 乘以 i，把它们的乘积划掉
                spf[i*p]=p
                isprime[i*p]=False
                
            # 【欧拉筛的灵魂核心！！！】
            # 如果 i 已经被当前的质数 p 整除，立刻打断循环！
            # 绝对不能再用后面的质数去乘这个 i 了！
                if i%p==0:
                    break
        return prime,spf# 返回收集到的所有质数,以及所有数最大质因子
```

沿最小质因子表反复整除，得到质因数列表

```python
##spf可以拿来极限质因数分解
    def factorization(x,spf):
        factors=[]
        while x>1:
            minfactor=spf[x]
            factors.append(minfactor)
            x//=minfactor
        return factors
```

平方根试除与 6k±1 的推导

```python
##素数判断
##只要在 [2, √n] 中找到第一个因子（第二个自动会出来）
##n 就不是素数
##法一
from math import isqrt
T=int(input())
for _ in range(T):
    n=int(input())
    print("Yes" if n>1 and all(n%i!=0 for i in range(2,isqrt(n)+1)) else "No")
##法二
##所有自然数都可以表示为 6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5 （k>= 0）的形式。
##6k, 6k+2, 6k+4 一定是偶数，能被 2 整除。6k, 6k+3 一定能被 3 整除。
##因此，当 n >= 5 时，所有的素数必定分布在 6k+1 或 6k+5（即 6k-1）的形式中。
##这步推导意味着什么？
##意味着我们在写 for 循环找因子时，可以避开所有2和3的倍数，每次循环直接让步长跳跃 6！
##这使得测试因子的数量直接缩小到原来的三分之一。
```

埃氏筛的循环边界草稿

```python
##挨氏筛
import math
isp=[True]*(n+1)
isp[0]=isp[1]=False
p=[]
for i in range(2,math.isqrt(n)+1):
    if isp[i]:
        for j in range(i**2,i,m+1):
            isp[j]=False
for i in range(2,n+1):
    if isp[i]:p.append(i)
```

<a name="knowledge-digits"></a>

### 整数拆位与数位和

用取余和整除提取个位、十位

```python
##带余除法####################################################################
a=int(input())
print(a%10)
    
##整数的十位########################################################################
a=int(input())
if a//10==0:
    print('0')
else:
    a//=10
    print(a%10)
```

对字符串中的各位求和

```python
#####位数和################################################################
a=input()
s=sum(int(i) for i in a)
print(s)
```

把秒数拆为时、分、秒

```python
#####时间转换################################################################
##a=int(input())
##b=a//3600
##c=(a-b*3600)//60
##d=a-b*3600-c*60
##print(b,c,d)
#更好的方法
a = int(input())
# 只改2个 / 为 //，其余不变
print("%d %d %d"%(a//3600, a%3600//60, a%60))#除余的概念
```

通过索引遍历数位并求和

```python
##数位之和
n=input()
print(sum(int(n[i]) for i in range(len(n))))
```

<a name="knowledge-sqrt"></a>

### 整数平方根

开平方并向下取整

```python
##平方根################################################################
from  math import sqrt,floor
a=int(input())
print(floor(sqrt(a)))#a=int(n**0.5)orprint(int(sqrt(n)))
```

<a name="knowledge-geo"></a>

### 坐标距离与三角形面积

欧氏距离、曼哈顿距离及其差值

```python
###绕距################################################################
from math import sqrt,fabs
grid=[list(map(int,input().split())) for _ in range(2)]
d1=sqrt((grid[0][0]-grid[1][0])**2+(grid[0][1]-grid[1][1])**2)
d2=fabs(grid[0][0]-grid[1][0])+fabs(grid[0][1]-grid[1][1])
d3=fabs(d1-d2)
print(format(d3,".9f"))
```

用叉积表示三角形面积

> 三角形已知三点坐标求面积：叉积绝对值的一半

<a name="knowledge-series"></a>

### 交错和与调和和

交替加减与倒数求和

```python
##牛牛学数列
n=int(input())
##print(sum+=i if i%2!=0 else -i for i in range(1,n+1))语法错了
s=sum(i if i%2!=0 else -i for i in range(1,n+1))
print(s)

##牛牛学数列2
n=int(input())
s=sum(1/i  for i in range(1,n+1))
print(f"{s:.6f}")
```

<a name="knowledge-countdig"></a>

### 数位出现次数

用 Counter、字符串拼接或逐数扫描统计出现次数

```python
from collections import Counter
a=[i for i in range(1,n+1)]
a=str(a)
c=Counter(a)
print(c[str(x)])
n,x=map(int,input().split())
a=''.join(str(i) for i in range(1,n+1))
##print(a.count('x'))
print(a.count(str(x)))
##更快
for i in range(1,n+1):
    ans+=str(i).count(str(x))
```

按高位、当前位、低位计数的第一版

> 1到n有多少0   位数取数本质

```python
n,x=map(int,input().split())
step=1
while step<=n:
    hs,ls=n//step,n%step
    c=hs%10
    if c>x:
        ans+=(hs//10+1)*step
    elif c==x:
        ans+=(hs//10)*step+ls+1
    else:
        ans+=(hs//10)*step
    if not x:
        ans-=step
    step*=10
print(cnt)
```

第二次推演整除、取余与按位取数

```python
step=1
while step<=n:
    hs,ls=n//step,n%step
    c=hs%10
    if c>x:
        ans+=(hs//10+1)*step
    elif c==x:
        ans+=(hs//10)*step+ls+1
    else:
        ans+=(hs//10)*step
    if not x:
        ans-=step
    step*=10
print(ans)
```

> 本质2：// 的本质是“向右推移并丢弃”。// (整除操作符：十进制右移器)
> // 10的k次方 的物理意义就是**“抹掉数字最右边的 k 位”**。
> 在十进制里，你把一个数整除 10（// 10），它的本质效果就是把整个数字向右推了一位，
> 最右边的那位直接掉下悬崖摔碎了。
> 除以 100，就是往右推两位，掉下去两个。
> 本质3：% 的本质是“只保留最右边的尾巴”。
> % 10的k次方 的物理意义就是**“只保留数字最右边的 k 位，左边的全部清零屏蔽”**。
> 你对一个数取余 10（% 10），本质效果就是拿一把刀，贴着最后一位的左边切下去，
> 左边的主体全扔掉，只保留切下来的最后一位。    
> 合体必杀技： 如果我们想精准拿到某一位（比如百位），怎么做？
> 第一步：用 // 100，把百位右边的数字全部推下悬崖，
> 此时原来的“百位”就变成了新的“个位”（最后一位）。
> 第二步：用 % 10，一刀切下去，把新个位左边的数字全扔掉。
> 完美拿到了百位！

<a name="knowledge-pow"></a>

### 模幂运算

内置 pow 的三参数形式

> 杀手八：幂模运算只用内置pow(a,b,c)

<a name="knowledge-digitstr"></a>

### 拼接整数序列的第 n 位

按位数划分区间的初稿

```python
n=int(input())
if n<10:
    print(n)
elif 10<=n<180:
    n-=9
    n
```

用整除和取余定位两位数及其数位

>  你正在尝试的数学解法（极其容易写错边界）

```python
n = int(input())
if n <= 9:
    print(n)
elif n <= 189:
    n -= 9  # 扣除掉1位数的9个字符
    # 剩下的 n，是在 "10111213..." 这个纯2位数序列里的找第 n 个字符
    # (n-1)//2 算出是第几个数字，(n-1)%2 算出是这个数字里的第几位
    num = 10 + (n - 1) // 2 
    digit_idx = (n - 1) % 2
    print(str(num)[digit_idx])
else:
    # 还要继续写 3 位数的逻辑... (190 到 2889)
    pass    
```

逐个拼接与一次 join 后按索引取位

```python
n = int(input())

s = ""
for i in range(1, 1001):
    s += str(i)  # 暴力把数字转成字符串拼起来

 字符串的索引是从 0 开始的，所以第 n 个字符的索引是 n-1
print(s[n-1])

n = int(input())

 瞬间生成 "1234567891011..."
s = "".join(map(str, range(1, 1001))) 

print(s[n-1])
```

编排参考 [开放 CS/AI 知识库的 Python 代码模板](https://wiki.dwj601.cn/ds-and-algo/templates-py/)。
