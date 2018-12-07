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

**filter函数时候后，返回的是一个filter的对象（一个Iterator,是一个惰性序列，如果需要返回所有计算的结果，需要使用list()函数获得所有结果并返回list。)**

### 例子：写一个素数序列
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

这个程序当时写的时候，一开始没写起来，后来自己写的有点问题，看下思路吧：

* 首先定义一个返回奇数的列表的生成器。从3开始。因为对于素数来说，第一步就是取2，并且把2的倍数删除掉，所以偶数在素数中是不存在的。那么直接从奇数开始删选。
* 然后有定义了一个生成器，这个生成器的作用是过滤掉3，5，7，9，依次类推他们的倍数，并且返回他们本身，这边看到生成器有个好处，那就是在函数中循环前，生成器可以返回一个值，这样就可以把那些不符合规律的东西放在这边，作为返回值。并且这个东西是可以放很多的，你可以放置yield 55，yield 33。生成器的好处就是作为一个序列，在函数中，在循环前，可以做你想要做的事情，在循环中，你可以按照规矩去办事情。并且，给你断点的权利，调用next的时候，会从断点处继续，你在循环外，你就执行下一行，你在循环中，你就执行循环中的下一行。
* 注意这里面，我们将奇数生成器odd_list()，赋值给g，我们只可以调用next(odd_list()),而不是next(odd_list)。
* 生成器还有个好处就是规定了循环体的新的循环一次的结束点。原来是循环体执行到最后一句进行下一次循环，现在是循环体，执行到yield就停止，等待下一次的被调用。
```python
>>> def odd_list():
...     n=1
...     while True:
...             n=n+2
...             yield n
...
>>> odd_list
<function odd_list at 0x0025A6F0>
>>> odd_list()
<generator object odd_list at 0x00293F90>
```
可以看到如果我们不加括号，那么这个只是一个函数，如果加了括号，那么他就是一个生成器了。
* 返回该值，并且将他的倍数都通过filter去除掉，除以该数，余数大于0的，说明不是他的倍数，返回都是True，这个时候将这些数保留并且将过滤过一遍的列表赋值给下次循环返回的值的新列表。
* 记住，生成器是一个可迭代的对象。对于生成器序列中的每一个值，我们要做一次判断，判断该值的大小，然后输出该值。

练习：
```python
def is_palindrome(n):
    s = str(n)
    # print(s)
    if len(s)==1:
        return True
    else:
        lst = [c for c in s]
        # print(lst)
        for i in range(len(lst)):
            if lst[i]==lst[len(lst)-i-1]:
                return True
            else:
                return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

```

网上还看到一种我没想到的解法，回文串就是把字符串反过来跟原字符串应该是相等的。
```python
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
```
这种切片的写法是相当简单的。四行就搞定了。

还有一种写法
```python
def is_palindrome(n):
    s=str(n)
    if len(s)==1:
        return True
    else:
        lst = [c for c in s]
        new_list = []
        for x in range(len(lst)):
            new_list.append(lst[len(lst)-x-1])
        if (''.join(new_list))==s:
            return True
        else:
            return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
```
这里面有把int转换为str，把str转换为list，把列表转换为str。


---
# 涉及到补充知识点：

## str() 会怎么样
str()这个函数
```python
>>> str([1,2,3,4])
'[1, 2, 3, 4]'
>>> a= str([1,2,3,4])
>>> a[1]
'1'
>>> a
'[1, 2, 3, 4]'
>>> a[2]
','
>>> a[0]
'['
```
str(),就是将传入的object，str化，如果传入的是列表，那么连列表里面的符号都会变成str中的的元素。对传入的对象两边加上双引号，表示这个是一个字符串。

## list() 会怎么样
list() 也是一个类型构造器，他构造的是将传入的对象，转换为list，包括其中的特殊符号。
```python
>>> list('21')
['2', '1']
>>> list('nid.ddkj'
... )
['n', 'i', 'd', '.', 'd', 'd', 'k', 'j']
```

## join() && strip()
* join 
看下python3 cookbook中的“2.14章节 合并拼接字符串”

* strip 
strip是一个字符串用后面的分割符号进行分割，最后组成一个list返回。
```python
>>> '1-2-3-4'.split('-')
['1', '2', '3', '4']
>>> '1,2,3'.split(',')
['1', '2', '3']
```

## 双冒号的用法
见《廖雪峰课程》中的高级特性-切片。
