# 位运算与子集

[主题目录](README.md) · [浅色阅读页](index.html#bits)

让每一位表示是否选中一个元素，用掩码查询、修改或枚举整个集合。

- [用整数表示集合](#note-tsingpigdadademoban-1002)
- [按位枚举配料子集](#note-dfs-722)

<a name="note-tsingpigdadademoban-1002"></a>

## 用整数表示集合

查位、置位、清位、判空、判满与翻转的六条速记

原稿 [Tsingpigdadademoban.py · L1002–1026](originals/Tsingpigdadademoban.py#L1002-L1026)

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
> 
> 


<a name="note-dfs-722"></a>

## 按位枚举配料子集

关联知识点 · [配料的酸度与苦度](dfs.md#note-dfs-610)

从非空子集到整数掩码的原始笔记

原稿 [dfs.py · L722–724](originals/dfs.py#L722-L724)

> 对于数学系学生来说，集合的子集和二进制数构成了完美的双射（Bijection）。
> $n$ 个物品的选与不选，完美对应 $0 \sim 2^n - 1$ 的每一个整数的二进制位。
> 这彻底消灭了函数调用的开销，速度提升极限！

逐位累计酸度积与苦度和，和同题的 DFS 写法对读

原稿 [dfs.py · L725–771](originals/dfs.py#L725-L771)

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
