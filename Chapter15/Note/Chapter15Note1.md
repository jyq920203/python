# 15.1 time模块
内置的time模块让Python程序能读取当前时间，
在time模块中time.time()和time.sleep()函数是最有用的模块

## 15.1.1 time.time()函数
Unix纪元是变成中经常参考的时间：1970年1月1日0点，UTC时间，协调世界时间
time.time()是自那一刻以来的秒数，是一个浮点值（就是带小数点的数），
这个数字叫做Unix时间戳
```python
import time
time.time()
```
纪元时间戳可以用于剖析代码，测量一段代码执行的时间，在代码开始的时间调用
time.time(),在结束的时间再次调用，可以用第二个时间戳减去第一个时间戳，就是
两次调用之间经过的时间

## 15.1.2 time.sleep()函数
让程序暂停一下，就调用time.sleep()函数，并传入希望暂停的秒数。
在Idle中按住ctrl+c并不会中点time.sleep()的调用，IDLE会等待到暂停结束，在抛出
KeyboardInterrupt异常，要绕过这个问题，不要一次调用暂停30s，而是要使用for循环
执行30次time.sleep(1)调用
```python
import time
for i in range(30):
    time.sleep(1)  
```
这时候在30s内按ctrl+c，应该马上就抛出KeyboardInterrupt异常

