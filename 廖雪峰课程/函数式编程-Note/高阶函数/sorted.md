python内置函数可以对list进行排序,对数字可以进行从小到大的排序。
```python
sorted([36,5,-12,78])
[-12, 5, 36, 78]
```
sorted 同样也是一个高阶函数，还可以接受一个key函数来实现自定义的排序，例如可以按照绝对值进行排序，key指定的函数会作用于list的每一个元素上，并根据key函数返回的值，再进行排序。
```python
sorted([35,-8,90,-23],key=abs)
[-8, -23, 35, 90]
```
对字符串进行排序，是根据ASCII的大小来进行排序的。
```python
sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```
结果是大写的Z，要排列在小写的a前面，因为大写字母的ASCII码数字比小写字母的要小。
所以如果要忽略大小写进行排序的话，那么就要将列表中统一为大写或者统一为小写字母，这样就是按照字母顺序进行排列的了。
```python
sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper)
['about', 'bob', 'Credit', 'Zoo']
sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

如果要进行反向排序的话，我们不需要修改key函数，只要传入第三个参数`reverse=True`:
```python
sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```
sorted是一个高阶函数，他排序的关键在于实现一个映射函数。

给出一个学生跟分数的tuple组成的list，请按照学生的姓名进行排序：
```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    for key in t:
        return key[0]

L2 = sorted(L, key=by_name)
print(L2)
```
结果返回：
```python
[('Adam', 92), ('Bob', 75), ('Bart', 66), ('Lisa', 88)]
```