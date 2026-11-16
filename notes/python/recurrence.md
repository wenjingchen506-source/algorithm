# 递推与组合计数

[主题目录](README.md) · [浅色阅读页](index.html#recurrence)

同一道跳台阶题，从递归、滚动变量、特征方程和组合计数四个角度看。

- [跳台阶](#note-dfs-9)

<a name="note-dfs-9"></a>

## 跳台阶

题目与第一种思路

原稿 [dfs.py · L9–10](originals/dfs.py#L9-L10)

> ##跳台阶https://www.acwing.com/problem/content/823/
> 法一

递归求 f(n−1) 与 f(n−2) 的和

原稿 [dfs.py · L11–23](originals/dfs.py#L11-L23)

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

原稿 [dfs.py · L24–25](originals/dfs.py#L24-L25)

> 法二：特征方程求解（c1+c2*n）*r^n或c1*r1^n+c2*r2^n
> 法三

用两个变量滚动更新相邻项

原稿 [dfs.py · L26–35](originals/dfs.py#L26-L35)

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

原稿 [dfs.py · L36–38](originals/dfs.py#L36-L38)

> 法四：设走k个2级台阶，则走了2k步，剩下走n-2k个一级台阶，总共k+n-2k=n-k种选法，
> c(k,n-k)且k<=[n/2]
> 
