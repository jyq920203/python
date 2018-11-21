filter()是一个高阶函数，接受一个函数还有一个序列。
这个函数可以作为序列的过滤器，根据返回的东西是True还是False来判断这个东西是不是要舍弃这个元素，返回True的保留，False的舍弃。


```python
def is_odd(n):
    return n%2 == 1

print(filter(is_odd,[1,2,3,4,5,6]))

print(list(filter(is_odd,[1,2,3,4,5,6])))
```

结果：
```python
<filter object at 0x0220BD30>
[1, 3, 5]
```

filter函数时候后，返回的是一个filter的对象（一个Iterator,是一个惰性序列，如果需要返回所有计算的结果，需要使用list()函数获得所有结果并返回list。)

```python
def odd_list():
    n=1
    while True:
        n= n+2
        yield n

def su_filter():
    yield 2
    g = odd_list()
    while True:
        it = next(g)
        yield it
        g = filter(lambda n,it=it:n%it>0,g)

for n in su_filter():
    if n < 20:
        print(n)
    else:
        break
```

结果：
```python
2
3
5
7
11
13
17
19
```