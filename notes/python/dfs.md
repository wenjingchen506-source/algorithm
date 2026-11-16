# DFS、枚举与回溯

[主题目录](README.md) · [浅色阅读页](index.html#dfs)

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

## 递归深度与缓存

调整解释器的递归上限

原稿 [Tsingpigdadademoban.py · L37–38](originals/Tsingpigdadademoban.py#L37-L38)

```python
sys.setrecursionlimit(1000000)

```

记忆化装饰器片段

原稿 [Tsingpigdadademoban.py · L1047–1050](originals/Tsingpigdadademoban.py#L1047-L1050)

```python
@lru_cache(maxsize=None)



```


<a name="note-tsingpigdadademoban-313"></a>

## 装箱与最少工作时段

任务从大到小放入已有时段，或新开时段并回溯

原稿 [Tsingpigdadademoban.py · L313–335](originals/Tsingpigdadademoban.py#L313-L335)

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

## 逐位搜索最大数

记录当前数位和两类剩余操作次数，探索各分支

原稿 [Tsingpigdadademoban.py · L480–508](originals/Tsingpigdadademoban.py#L480-L508)

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

## 记录方案与恢复现场

为什么可变路径要保存快照

原稿 [Tsingpigdadademoban.py · L531–534](originals/Tsingpigdadademoban.py#L531-L534)

> 带着 [1, 2] 进入下一层，立刻记录 [1, 2]。
> 只要是把一个“会随着时间变化的数据容器（列表、字典、集合）”塞进结果集里，
> 绝对、必须、永远要加上 .copy()！
> 否则你塞进去的，只是一个会随时爆炸的定时炸弹。

列表引用的实验

原稿 [Tsingpigdadademoban.py · L535–540](originals/Tsingpigdadademoban.py#L535-L540)

```python
path = [1]         # 第一步：我有一个列表，里面装了 1
ans = []           # 第二步：我有一个空的结果集
ans.append(path)   # 第三步：我把 path 塞进了 ans
path.append(2)     # 第四步：我往 path 里又加了一个 2

print(ans)         # 请问，现在打印 ans，结果是什么？
```

列表引用、递归返回与 pop 的原始笔记

原稿 [Tsingpigdadademoban.py · L541–557](originals/Tsingpigdadademoban.py#L541-L557)

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
> 

把路径用 join 存成字符串的例子

原稿 [dfs.py · L110–123](originals/dfs.py#L110-L123)

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
> 

何时把当前路径记入答案

原稿 [dfs.py · L149–157](originals/dfs.py#L149-L157)

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

## 组合枚举

固定选 k 个数，按每个数选或不选递归

原稿 [Tsingpigdadademoban.py · L558–573](originals/Tsingpigdadademoban.py#L558-L573)

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

原稿 [dfs.py · L124–148](originals/dfs.py#L124-L148)

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

## 组合总和

排序后从当前下标继续选，允许重复使用候选数

原稿 [Tsingpigdadademoban.py · L574–594](originals/Tsingpigdadademoban.py#L574-L594)

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

## 子集枚举

指数型枚举。对照原稿中的递归树跟踪选与不选

原稿 [dfs.py · L39–78](originals/dfs.py#L39-L78)

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

## 排列枚举

洛谷 P1706。用访问标记与路径生成排列

原稿 [dfs.py · L79–109](originals/dfs.py#L79-L109)

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

## 选数与素数和

关联知识点 · [素数判定与分解](math.md#note-tsingpigdadademoban-80)

洛谷 P1036。读入 n、k，准备结果与路径

原稿 [dfs.py · L158–167](originals/dfs.py#L158-L167)

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

原稿 [dfs.py · L265–293](originals/dfs.py#L265-L293)

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

## 烤鸡的定长枚举

洛谷 P2089。十种配料的取值范围与方案总数

原稿 [dfs.py · L294–301](originals/dfs.py#L294-L301)

> 烤鸡https://www.luogu.com.cn/problem/P2089
> 这道题的本质是把一个数字n拆分成10个数字的和，且每个数字只能取1,2,3。
> 第一重识破（数学陷阱）：10种配料，每种最少1克，最多3克。
> 这意味着美味程度的总和最小是10，最大是30！
> 如果输入的n<10或者n>30，绝对不可能拼出来，直接输出0即可。
> 第二重识破（暴力极限）：既然有10个坑位，每个坑位有3种选择，
> 那么全宇宙的方案总数就是3^{10}=59049种。
> 区区不到6万种状态，连给计算机塞牙缝都不够，直接无脑枚举！

用 itertools.product 枚举十个位置

原稿 [dfs.py · L302–317](originals/dfs.py#L302-L317)

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

原稿 [dfs.py · L318–355](originals/dfs.py#L318-L355)

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

## 火星人与字典序后继

洛谷 P1088。交换升序断点并反转后缀，逐次得到下一排列

原稿 [dfs.py · L356–378](originals/dfs.py#L356-L378)

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

原稿 [dfs.py · L379–444](originals/dfs.py#L379-L444)

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

原稿 [dfs.py · L445–522](originals/dfs.py#L445-L522)

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

原稿 [dfs.py · L523–560](originals/dfs.py#L523-L560)

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

## 火柴加法

洛谷 P1149。预计算数字的火柴数，枚举加数并检查等式

原稿 [dfs.py · L561–609](originals/dfs.py#L561-L609)

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

## 配料的酸度与苦度

关联知识点 · [按位枚举配料子集](bits.md#note-dfs-722)

带 haschosen、参数与作用域讨论的调试草稿，保留报错写法

原稿 [dfs.py · L610–677](originals/dfs.py#L610-L677)

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

原稿 [dfs.py · L678–721](originals/dfs.py#L678-L721)

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
