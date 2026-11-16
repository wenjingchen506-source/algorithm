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

<a name="topic-io"></a>

## 竞赛输入输出与文件

先看标准输入的入口，再对照读文件、重定向和逐行解析的写法。

- [竞赛快读与输出](#note-tsingpigdadademoban-1)
- [本地文件与标准流切换](#note-tsingpigdadademoban-882)
- [文件题的读写方式](#note-tsingpigdadademoban-920)

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

<a name="topic-structure"></a>

## 数据结构与计数

用集合删去已处理的元素，用频次表记录配对次数，或用抵消计数维护候选值。

- [多数元素与摩尔投票](#note-tsingpigdadademoban-95)
- [哈希集合与连续序列](#note-tsingpigdadademoban-245)
- [从双倍数组还原](#note-tsingpigdadademoban-263)

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

<a name="topic-binary"></a>

## 二分与答案边界

先写出候选值的可行条件，再判断要找第一个可行值还是最后一个可行值。

- [冶炼金属的可行区间](#note-tsingpigdadademoban-366)
- [二分答案分糖果](#note-tsingpigdadademoban-466)

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

<a name="topic-recurrence"></a>

## 递推与组合计数

同一道跳台阶题，从递归、滚动变量、特征方程和组合计数四个角度看。

- [跳台阶](#note-dfs-9)

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

<a name="topic-bfs"></a>

## BFS 与最短步数

网格扩散与开关谜题共用按层扩展的写法，队列分别存坐标和灯光状态。

- [网格上的多源 BFS](#note-tsingpigdadademoban-595)
- [开关谜题的状态空间 BFS](#note-tsingpigdadademoban-705)

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

<a name="topic-math"></a>

## 数论与素数筛

从单次试除到批量筛选，再用前缀和做区间查询、用最小质因子表做分解。

- [筛法与区间计数](#note-tsingpigdadademoban-50)
- [素数判定与分解](#note-tsingpigdadademoban-80)

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

编排参考 [开放 CS/AI 知识库的 Python 代码模板](https://wiki.dwj601.cn/ds-and-algo/templates-py/)。
