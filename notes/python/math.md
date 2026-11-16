# 数论与素数筛

[主题目录](README.md) · [浅色阅读页](index.html#math)

从单次试除到批量筛选，再用前缀和做区间查询、用最小质因子表做分解。

- [筛法与区间计数](#note-tsingpigdadademoban-50)
- [素数判定与分解](#note-tsingpigdadademoban-80)

<a name="note-tsingpigdadademoban-50"></a>

## 筛法与区间计数

先标记合数，再通过前缀和回答闭区间内的合数个数

原稿 [Tsingpigdadademoban.py · L50–76](originals/Tsingpigdadademoban.py#L50-L76)

```python
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

```


<a name="note-tsingpigdadademoban-80"></a>

## 素数判定与分解

关联知识点 · [选数与素数和](dfs.md#note-dfs-158)

用奇数试除到整数平方根，调用前需要导入 isqrt

原稿 [Tsingpigdadademoban.py · L80–86](originals/Tsingpigdadademoban.py#L80-L86)

```python
def ip(n):
    if n==2 or n==3:return True
    if n&1!=1 or n<2:return False
    for i in range(3,isqrt(n)+1,2):
        if n%i==0:return False
    return True#老是忘记

```

选数题的三种判定需求与选型笔记

原稿 [dfs.py · L168–178](originals/dfs.py#L168-L178)

```python
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
    
```

朴素埃氏筛。这里的 isp 表供选数题的 DFS 主干查询

原稿 [dfs.py · L179–186](originals/dfs.py#L179-L186)

```python
##法一：挨氏筛MLE    
    import math
    isp=[True]*(sum(sz)+1)
    isp[0]=isp[1]=False
    for i in range(2,math.isqrt(sum(sz))+1):
        if isp[i]:
            for j in range(i**2,sum(sz)+1,i):
                isp[j]=False
```

试除法。排除小于 2 的数与偶数，再枚举奇因子

原稿 [dfs.py · L187–194](originals/dfs.py#L187-L194)

```python
##法二：试除法
    def isprime(n):
        if n==2 or n==3:return True
        if n<2 or not n&1:return False
        for i in range(3,math.isqrt(n)+1,2):
            if n%i ==0:
                return False
        return True
```

用 bytearray 做切片埃氏筛，推导替换的字节数

原稿 [dfs.py · L195–216](originals/dfs.py#L195-L216)

```python
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
```

切片筛重写草稿。第 224 行把切片的冒号写成了逗号

原稿 [dfs.py · L217–226](originals/dfs.py#L217-L226)

```python
## prime 是我们在这行代码里“现场起的名字”，它来源于 enumerate 吐出来的数据！
    def jsaishishai(n):
        isprime=bytearray([1])*(n+1)
        isprime[0]=isprime[1]=0
        for i in range(2,math.isqrt(n)+1):
            if isprime[i]:#######
                length=(n-i*i)//i+1
                isprime[i*i,n+1,i]=bytearray([0])*length
        return [i for i,prime in enumerate(isprime) if prime]
    
```

欧拉筛与最小质因子表草稿。第 237 行判定要核对 spf 和 isp

原稿 [dfs.py · L227–254](originals/dfs.py#L227-L254)

```python
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
```

沿最小质因子表反复整除，得到质因数列表

原稿 [dfs.py · L255–264](originals/dfs.py#L255-L264)

```python
##spf可以拿来极限质因数分解
    def factorization(x,spf):
        factors=[]
        while x>1:
            minfactor=spf[x]
            factors.append(minfactor)
            x//=minfactor
        return factors


```
