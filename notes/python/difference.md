# 前缀和与差分

[主题目录](README.md) · [浅色阅读页](index.html#difference)

把一次区间更新记录在两个端点上，再通过前缀和恢复每个位置的覆盖次数。

- [区间覆盖与前缀和](#note-tsingpigdadademoban-350)
- [二分定位与差分计数](#note-reshensaibaiduzhixing-1)

<a name="note-tsingpigdadademoban-350"></a>

## 区间覆盖与前缀和

把每个数可调整的范围视为区间，用差分求最大重叠数

原稿 [Tsingpigdadademoban.py · L350–365](originals/Tsingpigdadademoban.py#L350-L365)

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

## 二分定位与差分计数

百度之星热身赛。用左右二分定位闭区间，再按覆盖次数模 4 分组，含手写输入样例

原稿 [reshensaibaiduzhixing.py · L1–46](originals/reshensaibaiduzhixing.py#L1-L46)

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
