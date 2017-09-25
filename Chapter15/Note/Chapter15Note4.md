# 15.4 datetime模块
time模块用于获取Unix的纪元时间戳，如果是为了更方便的格式显示日期，
或者对日期进行算数运算，就应该使用datetime模块。
datetime模块有自己的datetime数据类型
```python
import datetime
datetime.datetime.now()
#结果：datetime.datetime(2017, 9, 25, 14, 40, 5, 326870)

dt = datetime.datetime.now()
dt.hour
#结果：14
```
datetime.datetime.now()返回一个datetime对象，这个对象包含了年月日时分秒和微秒
Unix纪元时间戳可以通过datetime.datetime.fromtimestamp()，转换为datetime对象
```python
import  datetime
datetime.datetime.fromtimestamp(100000000)
#结果：datetime.datetime(1973, 3, 3, 17, 46, 40)

```
表达式datetime.datetime.now()和datetime.datetime.fromtimestamp(time.time())做的事情是一样的，都返回
当前时刻的datetime对象
```python
import time
datetime.datetime.fromtimestamp(time.time())
#结果：datetime.datetime(2017, 9, 25, 14, 46, 28, 665169)

```
datetime对象可以用比较操作符进行比较，弄清楚谁在前面(晚)，后面的datetime对象是“更大”的值
```python
import datetime
halloween2015 = datetime.datetime(2015,10,31,0,0,0)
newyear2016= datetime.datetime(2016,1,1,0,0,0)
oct31_2015=datetime.datetime(2015,10,31,0,0,0)
halloween2015>newyear2016


halloween2015==newyear2016
#output: False
newyear2016 != oct31_2015
#output: True
halloween2015>newyear2016
#output: False

```
