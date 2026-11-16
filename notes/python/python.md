# Python 基础与常用 API

[主题目录](README.md) · [浅色阅读页](index.html#python)

从字符串查找、字典计数到表达式，按操作查找原来的小实验。

- [字符串、列表与映射](#note-tsingpigdadademoban-7)
- [字典与频次统计](#note-tsingpigdadademoban-14)
- [表达式与可迭代对象](#note-tsingpigdadademoban-39)
- [字符串赋值与循环](#note-rthsrth-1)

<a name="note-tsingpigdadademoban-7"></a>

## 字符串、列表与映射

首次出现的位置、矩阵展平与 find

原稿 [Tsingpigdadademoban.py · L7–13](originals/Tsingpigdadademoban.py#L7-L13)

```python
# 返回 string 指定范围中 str 首次出现的位置
list(map(s.index,s))  # 返回字符索引数组，返回的是第一次出现的索引！如 "abcba"-> [0,1,2,1,0]

c=[e for row in matrix for e in row]

s.find(obj)#找不到返回-1，不会报错

```

对两个序列逐项求和

原稿 [Tsingpigdadademoban.py · L31–32](originals/Tsingpigdadademoban.py#L31-L32)

```python
map(lambda x,y :x+y,[1,2],[3,4])

```


<a name="note-tsingpigdadademoban-14"></a>

## 字典与频次统计

默认值、字符权重与频次草稿。dict.get 的默认值应以位置参数传入，Couter 是原稿的拼写

原稿 [Tsingpigdadademoban.py · L14–30](originals/Tsingpigdadademoban.py#L14-L30)

```python
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


```


<a name="note-tsingpigdadademoban-39"></a>

## 表达式与可迭代对象

range 长度与按条件调用 lambda 的速记

原稿 [Tsingpigdadademoban.py · L39–42](originals/Tsingpigdadademoban.py#L39-L42)

```python
length=[(end-start)//step]针对range(start,end,step)

(lambda :print('no'),lambda :print('yes'))[sum(l)/len(l)<60]()末尾括号立马调用函数

```

过滤含 4 的数和 4 的倍数。此行的 map 与 filter 括号仍是草稿

原稿 [Tsingpigdadademoban.py · L77–79](originals/Tsingpigdadademoban.py#L77-L79)

```python
a='\n'.join(map(str(x),filter(lambda x: x%4!=0 and '4' not in str(x)),range(1,n+1)))


```


<a name="note-rthsrth-1"></a>

## 字符串赋值与循环

变量重新绑定与持续输出实验。原稿的 while True 会一直打印

原稿 [rthsrth.py · L1–6](originals/rthsrth.py#L1-L6)

```python
a='abc'

b=a
a='def'
while True:
    print('陈文静是大美女')
```
