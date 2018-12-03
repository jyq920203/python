
## 获取当前时间

* datatime是个模块名称也是个datetime模块下类的名称，所以导入的时候写的是`from datetime import datetime`
* datetime.now()可以返回当前的时间和日期。返回的是一个datetime的对象
* print(timedate对象)会获取一个字符串类型的时间

```python
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2018, 12, 3, 15, 54, 45, 890114)
>>> now = datetime.now()
>>> print(now)
2018-12-03 15:55:37.959114
>>> print(type(now))
<class 'datetime.datetime'>
```

## datetime转换为str

* 如果有一个datetime的对象，是可以把他格式化为你想要的格式的字符串时间的。
* 调用的方法是strftime()来实现的
* %a %b 可以参考下[python官方文档](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)


```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now.strftime('%a, %b %d %H:%M'))
Mon, Dec 03 16:03
>>>
```

