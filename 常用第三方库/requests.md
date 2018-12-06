

## 查看resp的编码encoding信息
可以查看在requests发送请求后，可以调用返回体的encoding，来查看返回的编码信息，然后也可以直接对这个encoding进行赋值，来对返回体进行编码。
可以参考[响应内容](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id3)章节

```python
import requests
resp=requests.get('http://reportdocs.static.szse.cn/files/text/etfdown//modules/report/views/eft_download_new.html?path=/files/text/ETFDown/&filename=pcf_159003_20181206;159003ETF20181206&opencode=ETF15900320181206.txt')
print(resp.encoding)
```

结果是：
```python
ISO-8859-1
```

## 超时

requests发送请求的时候可以在参数中假如一个timeout参数，这个参数作用的就是设置，这个参数设置的是连接过程的时间，并不是下载内容的时间，如果没有在指定的时间内，连接成功，那么就会引发一个异常。更精确的说是在timeout内，没有从基础套接字中接受到任何字节的数据。

```python
>>> requests.get('http://github.com', timeout=0.001)
```