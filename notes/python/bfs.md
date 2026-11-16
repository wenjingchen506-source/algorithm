# BFS 与最短步数

[主题目录](README.md) · [浅色阅读页](index.html#bfs)

网格扩散与开关谜题共用按层扩展的写法，队列分别存坐标和灯光状态。

- [网格上的多源 BFS](#note-tsingpigdadademoban-595)
- [开关谜题的状态空间 BFS](#note-tsingpigdadademoban-705)

<a name="note-tsingpigdadademoban-595"></a>

## 网格上的多源 BFS

起点、分层、入队标记与边界检查

原稿 [Tsingpigdadademoban.py · L595–614](originals/Tsingpigdadademoban.py#L595-L614)

> 二、 遇到 BFS，脑子里必须过电的 4 个考量要素
> 以后只要题目里出现“最短路径”、“最少步数”、“层层扩散”、
> “几天后蔓延到全图”这种字眼，立刻条件反射呼叫 BFS。
> 动手写代码前，必须拷问自己这 4 个问题：
> 1.起点是“单源”还是“多源”？
>     只有一个起点（走迷宫）：开局入队一个坐标。
>     有多个起点（病毒扩散、森林火灾）：开局遍历全图，把所有起点全部扔进队列！
> 2.需要“分层（时间概念）”吗？
>     如果题目问“能不能走到终点”，不需要分层，直接 while q:
>         无脑拿出来扩散就行。
>     如果题目问“第 k 天的状态”或“最少走几步”，必须严格分层，
>         必须加上 for _ in range(len(q)):，
>         并且在 for 循环外面加上步数/天数递增（你的代码里是 k -= 1）。
> 3.有没有严格的“入队即标记（判重）”？
>     绝对不能让同一个节点被重复扔进队列。
>     必须用一个 visited 集合，
>     或者像你这样直接修改原数组 g[nx][ny] = 1 来充当防重墙。
> 4.越界与合法性检查是否前置？
>     永远在“准备往队列里塞”的时刻（nx, ny），
>     立刻检查是否越过了长宽边界，是否是墙壁。        

长草初稿。源点坐标、边界判断和输出括号都有待修处

原稿 [Tsingpigdadademoban.py · L615–647](originals/Tsingpigdadademoban.py#L615-L647)

```python
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
```

长草修订版。收集所有初始草格，同时扩展 k 层

原稿 [Tsingpigdadademoban.py · L648–704](originals/Tsingpigdadademoban.py#L648-L704)

```python
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




    
```


<a name="note-tsingpigdadademoban-705"></a>

## 开关谜题的状态空间 BFS

关联知识点 · [用整数表示集合](bits.md#note-tsingpigdadademoban-1002)

用异或产生下一状态，入队前判重

原稿 [Tsingpigdadademoban.py · L705–709](originals/Tsingpigdadademoban.py#L705-L709)

```python
for mask in unique_effects:
    next_state = curr_state ^ mask
    if next_state not in visited:
        visited.add(next_state)
        q.append(next_state)
```

逐行推演开关动作与异或结果

原稿 [Tsingpigdadademoban.py · L710–757](originals/Tsingpigdadademoban.py#L710-L757)

> 第一句：for mask in unique_effects:
> 物理映射：你面前的桌子上，
> 摆着你在第一步预处理时提炼出来的所有“不重复的魔法面具（开关操作）”。
> 这行代码的意思是：“我要把桌子上的每一个按钮，全都试按一遍。”
> 
> 深度逻辑：在走迷宫时，这一步相当于 for dx, dy in 方向数组
> （尝试上下左右四个方向）。而在状态空间里，你的“方向”就是这些面具。
> 每一个 mask，代表着向一个全新的灯光状态迈进的可能。
> 
> 第二句：next_state = curr_state ^ mask
> 物理映射：按下按钮，见证奇迹！
> 
> 深度逻辑：这是最绝妙的一行位运算代码。^ 是异或符号，
> 它的铁律是：相同为 0，不同为 1。
> 
> 假设你摸到了一个 mask = 2（二进制 00010，代表翻转灯 1）。
> 
> 现在的房间 curr_state 是 00110。
> 
> 发生异或碰撞：
> 00110 (当前房间)
> 00010 (魔法面具)
> ------- (异或)
> 00100 (新房间 next_state)
> 
> 结果：原本亮着的灯 1（第 1 位）被面具里的 1 给“异或”成了 0（灭了）；
> 原本亮着的灯 2（第 2 位）碰到了面具里的 0，
> 保留了 1（继续亮着）。这行代码瞬间完成了多个灯泡的同时翻转，
> 并计算出了按完之后的新格局 next_state。
> 
> 第三句：if next_state not in visited:
> 物理映射：查验生死簿，防止死循环。
> 
> 深度逻辑：按完开关，房间变成了 next_state。
> 这时候你必须立刻停下来，翻开你手里的 visited 集合，
> 问自己一个问题：“这种灯光亮暗的组合，我以前是不是曾经踩出来过？”
> 
> 如果你在第 1 层就踩出过 00100，现在你到了第 5 层，
> 一顿操作后又搞出了 00100。
> 
> 这说明你刚才的操作纯属绕远路（脱裤子放屁）！
> 别人按 1 次就能达到的状态，你按了 5 次才达到，这绝对不可能是“最短路径”。
> 
> 只有当 next_state not in visited 成立
> （这是一种全宇宙首次发现的全新灯光格局），你才被允许进入下一步。
> 
> 
> 

原稿对照表：网格上的坐标与灯光的位掩码

原稿 [Tsingpigdadademoban.py · L758–770](originals/Tsingpigdadademoban.py#L758-L770)

> 概念            长草问题（物理网格 BFS）	开关谜题（状态空间 BFS）	         它的物理意义是什么？
> 当前位置        x, y = q.popleft()	curr_state = q.popleft()	我现在站在哪里？（现在的局面是什么）
>                   
> 尝试动作        for dx, dy in di:	for mask in unique_effects:	我下一步可以往哪走？（我可以按哪个开关）
> 
> 产生变化        nx = x + dx             next_state = curr_state ^ mask  执行动作后，到达的新地点 / 产生的新局面
>                 ny = y + dy
> 
> 防止回头        if grid[nx][ny] == 0:	if next_state not in visited:	这个新地点/新局面，我以前来过吗？
> 
> 登记入队        grid[nx][ny] = 1        visited.add(next_state)         没来过！赶紧打上标记，塞进队列明天处理
>                 q.append((nx, ny))      q.append(next_state)
>           

完整讲解版，按层搜索最少按键次数

原稿 [Tsingpigdadademoban.py · L771–837](originals/Tsingpigdadademoban.py#L771-L837)

```python
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

```

再写一遍。保留 op 的缩进与重复灯位的纠错记录

原稿 [Tsingpigdadademoban.py · L838–881](originals/Tsingpigdadademoban.py#L838-L881)

```python
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

```
