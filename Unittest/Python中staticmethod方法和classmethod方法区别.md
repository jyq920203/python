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






## Python的静态方法和类成员方法
参考http://www.cnblogs.com/2gua/archive/2012/09/03/2668125.html
Python的静态方法和类成员方法都可以被类或实例访问，两者概念不容易理清，但还是有区别的：
1）静态方法无需传入self参数，类成员方法需传入代表本类的cls参数；
2）从第1条，静态方法是无法访问实例变量的，而类成员方法也同样无法访问实例变量，但可以访问类变量；
3）静态方法有点像函数工具库的作用，而类成员方法则更接近类似Java面向对象概念中的静态方法。

如果上述执行过程太复杂，记住以下两点就好了：
静态方法：无法访问类属性、实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已。
类成员方法：可以访问类属性，无法访问实例属性。上述的变量val1，在类里是类变量，在实例中又是实例变量，所以容易混淆。


## python 类的实例方法，静态方法，类方法辨析和实例讲解
参考http://blog.csdn.net/a447685024/article/details/52424481
实例：可以调用实例方法，类方法，静态方法
类：不能调用实例方法，只能调用类方法和静态方法

静态方法不能访问类属性，所以这边用了类方法来实现。

## Meaning of @classmethod and @staticmethod for beginner?
参考：https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner?answertab=votes#tab-top
Though classmethod and staticmethod are quite similar, 
there's a slight difference in usage for both entities: 
classmethod must have a reference to a class object as the first parameter, 
whereas staticmethod can have no parameters at all.

#todo 没写完
#todo  
1.他们的区别是什么？
2.为什么要有他们？