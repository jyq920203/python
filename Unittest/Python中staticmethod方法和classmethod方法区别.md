Python中staticmethod方法和classmethod方法区别
参考：http://www.firefoxbug.com/index.php/archives/2818/
staticmethod和classmethod两种方法在python中是通过装饰器来实现的，语法
分别是@staticmethod 和@classmethod

## 定义方式差异
@classmethod和@staticmethod装饰方法时，对于被装饰方法本身定义有差异，主要体现在形参上
```python
@classmethod
# 第一个参数是类本身
def class_method(cls,data)

@staticmethod
#不存在任何与类、实例相关的参数，包括cls，self
def static_method(data)
```
## 调用方式差异
看看下面这个类
```python
class MyClass(object):
    def __init__(self):
        pass
    def normal_method(self,data):
        print("normal method:%s %s" %(self,data))
        
    @classmethod
    def class_method(cls,data):
        print("class method:%s %s" %(cls,data))
        
    @staticmethod
    def static_method(data):
        print("static method:%s" %(data))
```
正常情况下，调用类的方法前，必须要实例化
```python
>>> mc = MyClass()
>>> mc.normal_method("Hello World!")
normal method: <__main__.MyClass object at 0x10667c590> hello world!
```
normal_method(self,data)的第一个参数是self，python解释器会在运行时，自动把运行实例传递给被调用方法，
所以方法调用输出的结果是实例化object的内容。

### @classmethod调用
@classmethod装饰器实现功能是：类可以直接调用@classmethod装饰的方法，无需实例化

```python
>>> MyClass.class_method("hello world!")
class method: <class '__main__.MyClass'> hello world!
```
可以看到@classmethod装饰的函数cls变量被传递成类名

### @staticmethod调用
@staticmethod装饰器实现的功能是：无论类是否实例化，都可以直接调用@staticmethod修饰的函数
```python
#类直接调用
>>> MyClass.static_method("hello world!")
static method: hello world!
#类实例化后调用
>>>mc.static_method("hello world!")
static method: hello world!
```
## 使用场景
由于python本身是不支持函数的重载（顶多只能实现函数的取代），但是classmethod可以实现
类似重载的功能（虽然比较丑陋）
