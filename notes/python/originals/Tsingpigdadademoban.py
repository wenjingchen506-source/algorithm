import sys
def solve():
    da=iter(sys.stdin.read().split())
    n=int(next(da))
if __name__=='__main__':
    solve()
# 返回 string 指定范围中 str 首次出现的位置
list(map(s.index,s))  # 返回字符索引数组，返回的是第一次出现的索引！如 "abcba"-> [0,1,2,1,0]

c=[e for row in matrix for e in row]

s.find(obj)#找不到返回-1，不会报错

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


map(lambda x,y :x+y,[1,2],[3,4])

grid=[int(next(da)) for _ in range(m) for _ in range(n)]

sys.stdout.write('\n'.join(out)+'\n')

sys.setrecursionlimit(1000000)

length=[(end-start)//step]针对range(start,end,step)

(lambda :print('no'),lambda :print('yes'))[sum(l)/len(l)<60]()末尾括号立马调用函数

import sys
for line in sys.stdin:
    line=line.strip()

for line in sys.stdin:
    line=line.strip()

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

a='\n'.join(map(str(x),filter(lambda x: x%4!=0 and '4' not in str(x)),range(1,n+1)))


def ip(n):
    if n==2 or n==3:return True
    if n&1!=1 or n<2:return False
    for i in range(3,isqrt(n)+1,2):
        if n%i==0:return False
    return True#老是忘记

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans=[]
        for p in people:
            ans.insert(p[1],p)
        return ans

这道题的官方名字叫摩尔投票法。它把时间和空间复杂度压榨到了人类的物理极限：
O(N)时间，O(1)空间。
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

##LeetCode 1834
##LeetCode 218

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


带着 [1, 2] 进入下一层，立刻记录 [1, 2]。
只要是把一个“会随着时间变化的数据容器（列表、字典、集合）”塞进结果集里，
绝对、必须、永远要加上 .copy()！
否则你塞进去的，只是一个会随时爆炸的定时炸弹。
path = [1]         # 第一步：我有一个列表，里面装了 1
ans = []           # 第二步：我有一个空的结果集
ans.append(path)   # 第三步：我把 path 塞进了 ans
path.append(2)     # 第四步：我往 path 里又加了一个 2

print(ans)         # 请问，现在打印 ans，结果是什么？
按照人类的直觉，第三步塞进去的时候 path 是 [1]，所以最后 ans 应该是 [[1]]。

但是！在 Python 里运行的结果是：[[1, 2]]

为什么会发生这种“灵异事件”？
因为在 Python 中，像列表（List）这种可以不断变化的数据结构，
变量名其实只是一个“便利贴”（或者叫标签、指针），
它贴在了一块内存空间上。

递归的本质，就是“看剧时的暂停键”。
当你在 dfs(0) 的循环里走到 dfs(1) 时，
相当于你把正在看的《第一季》按下了暂停，跑去把《第二季》从头到尾全看完了，
然后解除暂停，继续看《第一季》剩下的剧情。

而那句看似没道理的 path.pop()，就是你每次看完后续剧情回来后，
必须把脑子里的杂念“清除”，才能继续看当下的剧情。

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
二、 遇到 BFS，脑子里必须过电的 4 个考量要素
以后只要题目里出现“最短路径”、“最少步数”、“层层扩散”、
“几天后蔓延到全图”这种字眼，立刻条件反射呼叫 BFS。
动手写代码前，必须拷问自己这 4 个问题：
1.起点是“单源”还是“多源”？
    只有一个起点（走迷宫）：开局入队一个坐标。
    有多个起点（病毒扩散、森林火灾）：开局遍历全图，把所有起点全部扔进队列！
2.需要“分层（时间概念）”吗？
    如果题目问“能不能走到终点”，不需要分层，直接 while q:
        无脑拿出来扩散就行。
    如果题目问“第 k 天的状态”或“最少走几步”，必须严格分层，
        必须加上 for _ in range(len(q)):，
        并且在 for 循环外面加上步数/天数递增（你的代码里是 k -= 1）。
3.有没有严格的“入队即标记（判重）”？
    绝对不能让同一个节点被重复扔进队列。
    必须用一个 visited 集合，
    或者像你这样直接修改原数组 g[nx][ny] = 1 来充当防重墙。
4.越界与合法性检查是否前置？
    永远在“准备往队列里塞”的时刻（nx, ny），
    立刻检查是否越过了长宽边界，是否是墙壁。        
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




    
for mask in unique_effects:
    next_state = curr_state ^ mask
    if next_state not in visited:
        visited.add(next_state)
        q.append(next_state)
第一句：for mask in unique_effects:
物理映射：你面前的桌子上，
摆着你在第一步预处理时提炼出来的所有“不重复的魔法面具（开关操作）”。
这行代码的意思是：“我要把桌子上的每一个按钮，全都试按一遍。”

深度逻辑：在走迷宫时，这一步相当于 for dx, dy in 方向数组
（尝试上下左右四个方向）。而在状态空间里，你的“方向”就是这些面具。
每一个 mask，代表着向一个全新的灯光状态迈进的可能。

第二句：next_state = curr_state ^ mask
物理映射：按下按钮，见证奇迹！

深度逻辑：这是最绝妙的一行位运算代码。^ 是异或符号，
它的铁律是：相同为 0，不同为 1。

假设你摸到了一个 mask = 2（二进制 00010，代表翻转灯 1）。

现在的房间 curr_state 是 00110。

发生异或碰撞：
00110 (当前房间)
00010 (魔法面具)
------- (异或)
00100 (新房间 next_state)

结果：原本亮着的灯 1（第 1 位）被面具里的 1 给“异或”成了 0（灭了）；
原本亮着的灯 2（第 2 位）碰到了面具里的 0，
保留了 1（继续亮着）。这行代码瞬间完成了多个灯泡的同时翻转，
并计算出了按完之后的新格局 next_state。

第三句：if next_state not in visited:
物理映射：查验生死簿，防止死循环。

深度逻辑：按完开关，房间变成了 next_state。
这时候你必须立刻停下来，翻开你手里的 visited 集合，
问自己一个问题：“这种灯光亮暗的组合，我以前是不是曾经踩出来过？”

如果你在第 1 层就踩出过 00100，现在你到了第 5 层，
一顿操作后又搞出了 00100。

这说明你刚才的操作纯属绕远路（脱裤子放屁）！
别人按 1 次就能达到的状态，你按了 5 次才达到，这绝对不可能是“最短路径”。

只有当 next_state not in visited 成立
（这是一种全宇宙首次发现的全新灯光格局），你才被允许进入下一步。



概念            长草问题（物理网格 BFS）	开关谜题（状态空间 BFS）	         它的物理意义是什么？
当前位置        x, y = q.popleft()	curr_state = q.popleft()	我现在站在哪里？（现在的局面是什么）
                  
尝试动作        for dx, dy in di:	for mask in unique_effects:	我下一步可以往哪走？（我可以按哪个开关）

产生变化        nx = x + dx             next_state = curr_state ^ mask  执行动作后，到达的新地点 / 产生的新局面
                ny = y + dy

防止回头        if grid[nx][ny] == 0:	if next_state not in visited:	这个新地点/新局面，我以前来过吗？

登记入队        grid[nx][ny] = 1        visited.add(next_state)         没来过！赶紧打上标记，塞进队列明天处理
                q.append((nx, ny))      q.append(next_state)
          
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


技巧 1：查看第 j 个物品有没有被用过
代码：if (S >> j) & 1 == 1:
    理解：把 S 的第 j 位推到最右边，然后和 1 进行“按位与”（&）。
    如果结果是 1，说明用过了。

技巧 2：把第 j 个物品标记为已用（本题讲解）
代码：S = S | (1 << j)理解：强行把第 j 位置为 1。

技巧 3：把第 j 个物品恢复为未用（回溯时常用）
代码：S = S & ~(1 << j)
理解：~ 是按位取反。制造一个“唯独第 j 位是 0，其他全是 1”的掩码，
用“按位与”把第 j 位强行清零。

技巧 4：判断是不是一个物品都没用过
代码：if S == 0:

技巧 5：判断是不是所有 $N$ 个物品全用完了
代码：if S == (1 << n) - 1:
理解：比如 $N=3$，1<<3 是 8（二进制 1000），
减去 1 就是 7（二进制 0111），恰好是前 3 位全为 1。
                             
技巧 6：改变状态
代码：S^(1<<j)


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


@lru_cache(maxsize=None)



