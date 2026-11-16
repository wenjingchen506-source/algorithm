# 数据结构与计数

[主题目录](README.md) · [浅色阅读页](index.html#structure)

用集合删去已处理的元素，用频次表记录配对次数，或用抵消计数维护候选值。

- [多数元素与摩尔投票](#note-tsingpigdadademoban-95)
- [哈希集合与连续序列](#note-tsingpigdadademoban-245)
- [从双倍数组还原](#note-tsingpigdadademoban-263)

<a name="note-tsingpigdadademoban-95"></a>

## 多数元素与摩尔投票

复杂度笔记

原稿 [Tsingpigdadademoban.py · L95–96](originals/Tsingpigdadademoban.py#L95-L96)

> 这道题的官方名字叫摩尔投票法。它把时间和空间复杂度压榨到了人类的物理极限：
> O(N)时间，O(1)空间。

计数抵消法，前提是多数元素存在。原稿缩进使用了全角空格

原稿 [Tsingpigdadademoban.py · L97–111](originals/Tsingpigdadademoban.py#L97-L111)

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

## 哈希集合与连续序列

从未处理的数向两侧扩展，删除属于同一段的元素

原稿 [Tsingpigdadademoban.py · L245–262](originals/Tsingpigdadademoban.py#L245-L262)

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

## 从双倍数组还原

排序后二分寻找一半，逐对移除

原稿 [Tsingpigdadademoban.py · L263–281](originals/Tsingpigdadademoban.py#L263-L281)

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

原稿 [Tsingpigdadademoban.py · L282–312](originals/Tsingpigdadademoban.py#L282-L312)

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
