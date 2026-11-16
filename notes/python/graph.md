# 图的表示与遍历

[主题目录](README.md) · [浅色阅读页](index.html#graph)

对照矩阵和邻接表存边的方式，再看沿后继搜索时如何记录访问深度。

- [沿后继搜索环](#note-tsingpigdadademoban-509)
- [带权无向图与 DFS](#note-tsingpigdadademoban-1027)

<a name="note-tsingpigdadademoban-509"></a>

## 沿后继搜索环

用字典记录访问深度的尝试。多个起点共用记录，跨轮次的深度差需要复核

原稿 [Tsingpigdadademoban.py · L509–530](originals/Tsingpigdadademoban.py#L509-L530)

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

## 带权无向图与 DFS

邻接矩阵、邻接表与遍历草稿。矩阵行初始化、DFS 形参与边的拆包顺序待核对

原稿 [Tsingpigdadademoban.py · L1027–1046](originals/Tsingpigdadademoban.py#L1027-L1046)

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
