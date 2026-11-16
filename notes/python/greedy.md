# 贪心与堆

[主题目录](README.md) · [浅色阅读页](index.html#greedy)

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

## 排序与插入

按身高降序、同身高按 k 升序重建队列

原稿 [Tsingpigdadademoban.py · L87–94](originals/Tsingpigdadademoban.py#L87-L94)

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

## 区间任务调度

按结束时间排序，优先把开机时段安排在区间右端

原稿 [Tsingpigdadademoban.py · L112–128](originals/Tsingpigdadademoban.py#L112-L128)

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

## 分段计算训练成本

按所需次数分组，每段比较集训价格与剩余单价总和

原稿 [Tsingpigdadademoban.py · L129–154](originals/Tsingpigdadademoban.py#L129-L154)

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

## 堆相关练习题号

原稿记下的 LeetCode 1834 与 218

原稿 [Tsingpigdadademoban.py · L155–157](originals/Tsingpigdadademoban.py#L155-L157)

```python
##LeetCode 1834
##LeetCode 218

```


<a name="note-tsingpigdadademoban-158"></a>

## 反悔贪心与堆

课程安排。超过截止时间时撤回耗时最长的课

原稿 [Tsingpigdadademoban.py · L158–169](originals/Tsingpigdadademoban.py#L158-L169)

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

原稿 [Tsingpigdadademoban.py · L170–187](originals/Tsingpigdadademoban.py#L170-L187)

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

原稿 [Tsingpigdadademoban.py · L188–207](originals/Tsingpigdadademoban.py#L188-L207)

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

## 利润与类别数的权衡

先选利润最高的 k 项，再用新类别替换重复类别

原稿 [Tsingpigdadademoban.py · L208–227](originals/Tsingpigdadademoban.py#L208-L227)

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

## 工资比例与最大堆

按工资质量比排序，用堆维护 k 人的质量总和

原稿 [Tsingpigdadademoban.py · L228–244](originals/Tsingpigdadademoban.py#L228-L244)

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

## 双指针配对

救生艇。让最重的人尝试与最轻的人同船

原稿 [Tsingpigdadademoban.py · L336–349](originals/Tsingpigdadademoban.py#L336-L349)

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
