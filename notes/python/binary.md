# 二分与答案边界

[主题目录](README.md) · [浅色阅读页](index.html#binary)

先写出候选值的可行条件，再判断要找第一个可行值还是最后一个可行值。

- [冶炼金属的可行区间](#note-tsingpigdadademoban-366)
- [二分答案分糖果](#note-tsingpigdadademoban-466)

<a name="note-tsingpigdadademoban-366"></a>

## 冶炼金属的可行区间

初稿。两处二分调用的括号未闭合

原稿 [Tsingpigdadademoban.py · L366–389](originals/Tsingpigdadademoban.py#L366-L389)

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

原稿 [Tsingpigdadademoban.py · L390–434](originals/Tsingpigdadademoban.py#L390-L434)

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

原稿 [Tsingpigdadademoban.py · L435–465](originals/Tsingpigdadademoban.py#L435-L465)

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

## 二分答案分糖果

枚举每人份量，按各堆能提供的份数判断可行性

原稿 [Tsingpigdadademoban.py · L466–479](originals/Tsingpigdadademoban.py#L466-L479)

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
