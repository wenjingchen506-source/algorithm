import sys
def solve():
    da=iter(sys.stdin.read().split())
if __name__=='__main__':
    solve()



##跳台阶https://www.acwing.com/problem/content/823/
法一
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
法二：特征方程求解（c1+c2*n）*r^n或c1*r1^n+c2*r2^n
法三
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
法四：设走k个2级台阶，则走了2k步，剩下走n-2k个一级台阶，总共k+n-2k=n-k种选法，
c(k,n-k)且k<=[n/2]

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
回想一下我们之前聊过的“连线”灾难：
如果你写的是 out.append(arr)，
那你就是往 out 里塞了一根指向 arr 这个木箱子的红线（内存引用）。
后续 arr.pop() 会把结果全毁掉。

但是！请死死盯住你写的 join 操作到底干了什么：
str(i) for i in arr：首先，它把篮子里的数字（比如 1 和 2），变成了字符 '1' 和 '2'。
' '.join(...)：然后，它用空格把这两个字符拼接起来，
在内存中凭空创造了一个全新的字符串对象："1 2"。
out.append("1 2")：最后，你把这个崭新的字符串，放进了 out 数组里。
真相大白：
在这段代码里，你根本没有把 arr 这个列表塞进结果集里！你是在每一次触底的时候，利用 join 自动把 arr 里的内容“冲洗成了一张固定的实物照片（字符串）”，
然后把照片放进了相册 out 里！

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
    
当你以后在考场上面对一道回溯题，不知道 res.append 该写在哪里时，
你只需要问自己一个问题：

“我当前手里拿着的这个半截 path，题目认不认它是一个合法的答案？”

如果认（比如求所有子集），那就一进函数，立刻拍照。

如果不认（必须要固定长度，或者必须要全部选完），
那就憋着，带着它继续往下走，直到满足条件（走到最后）了，再拍照。
####选数https://www.luogu.com.cn/problem/P1036
import sys
def solve():
    da=iter(sys.stdin.read().split())
    n,k=int(next(da)),int(next(da))
    sz=[int(next(da)) for _ in range(n)]
    ans=0
    out=[]
    arr=[]
    
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
    
##法一：挨氏筛MLE    
    import math
    isp=[True]*(sum(sz)+1)
    isp[0]=isp[1]=False
    for i in range(2,math.isqrt(sum(sz))+1):
        if isp[i]:
            for j in range(i**2,sum(sz)+1,i):
                isp[j]=False
##法二：试除法
    def isprime(n):
        if n==2 or n==3:return True
        if n<2 or not n&1:return False
        for i in range(3,math.isqrt(n)+1,2):
            if n%i ==0:
                return False
        return True
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
## prime 是我们在这行代码里“现场起的名字”，它来源于 enumerate 吐出来的数据！
    def jsaishishai(n):
        isprime=bytearray([1])*(n+1)
        isprime[0]=isprime[1]=0
        for i in range(2,math.isqrt(n)+1):
            if isprime[i]:#######
                length=(n-i*i)//i+1
                isprime[i*i,n+1,i]=bytearray([0])*length
        return [i for i,prime in enumerate(isprime) if prime]
    
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
##spf可以拿来极限质因数分解
    def factorization(x,spf):
        factors=[]
        while x>1:
            minfactor=spf[x]
            factors.append(minfactor)
            x//=minfactor
        return factors


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

烤鸡https://www.luogu.com.cn/problem/P2089
这道题的本质是把一个数字n拆分成10个数字的和，且每个数字只能取1,2,3。
第一重识破（数学陷阱）：10种配料，每种最少1克，最多3克。
这意味着美味程度的总和最小是10，最大是30！
如果输入的n<10或者n>30，绝对不可能拼出来，直接输出0即可。
第二重识破（暴力极限）：既然有10个坑位，每个坑位有3种选择，
那么全宇宙的方案总数就是3^{10}=59049种。
区区不到6万种状态，连给计算机塞牙缝都不够，直接无脑枚举！
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


对于数学系学生来说，集合的子集和二进制数构成了完美的双射（Bijection）。
$n$ 个物品的选与不选，完美对应 $0 \sim 2^n - 1$ 的每一个整数的二进制位。
这彻底消灭了函数调用的开销，速度提升极限！
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


















