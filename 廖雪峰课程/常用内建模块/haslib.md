## 摘要算法简介

摘要算法的定义：
摘要算法又叫做哈希算法，散列算法，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常是16进制的字符串表示）。
摘要算法通过摘要函数f()对任意长度data计算出固定长度digest，目的是为了发现原始数据是否被人篡改过。
摘要函数是一个单项的函数，计算f(data)很容易，但是通过digest反推data很困难，而且对原始数据做一个bit的修改，都会使得计算出来的摘要完全不同。
所以摘要函数可以用来校验数据有没有被人篡改过。


看下常见的md5的算法使用:

```python
import hashlib

md6 = hashlib.md5()
md6.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md6.hexdigest())
```
结果是`d26a53750bc40b38b65a520292f69306`

上面的程序可以求的`how to use md5 in python hashlib?`这个句话的md5值，记住先要编码成UTF-8，然后在求得`.hexdigest()`

如果你没有加`.encode('utf-8')`程序update的时候会报错

```python
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/ha.py", line 4, in <module>
    md6.update('how to use md5 in python hashlib?')
TypeError: Unicode-objects must be encoded before hashing
```

如果没有获取`.hexdigest()`，那么返回的只是一个md5的对象

```python
<md5 HASH object @ 0x0053B518>
```

如果字段很长也可以分段进行update
```python
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
```
结果是`d26a53750bc40b38b65a520292f69306`跟上面完整的是一样的。

当然也可以这么写不需要通过update:

```python
import hashlib

md9 = hashlib.md5('how to use md5 in python hashlib?'.encode('utf-8'))
print(md9.hexdigest())
```
也可以得到相同的结果。
MD5是最常见的摘要算法，速度很快，生成的结果是128bit，通常是一个32位的16进制字符串表示。






























```python
import hashlib

md9 = hashlib.md5('how to use md5 in python hashlib?'.encode('utf-8').hexdigest())
print(md9)
```