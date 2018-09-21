# 简述 __init__、__new__、__call__ 方法
参考：https://foofish.net/magic-method.html

对象有创建、初始化、使用、垃圾回收、不同的阶段由不同的方法（角色）来负责执行

## __init__方法
__init__方法负责对象的初始化，但是在系统执行该方法之前，其实该对象就已经存在了，不然
初始化什么东西呢？
```python
class A:
    def __init__(self):
        print("__init__")
        super(A,self).__init__()
        
    def __new__(cls):
        print("__new__")
        return super(A,cls).__new__(cls)
        
    def __call__(self):
        print("__call__")
        
A()
```
输出
```python
__new__
__init__
```
从结果来看__new__方法仙贝调用，返回一个实例对象，结果__init__被调用，__call__
方法并没有被调用

```python
def __init__(self):
    print("__init__")
    print(self)
    super(A,self).__init__()
    
def __new__(cls):
    print("__new__")
    self = super(A,cls).__new__(cls)
    print(self)
    return self
```
输出：
```python
__new__ 
<__main__.A object at 0x1007a95f8>
__init__ 
<__main__.A object at 0x1007a95f8>
```
从输出的结果看，__new__返回的就是类的实例对象，这个实例对象会传递给__init__方法定义的
self参数，以便实例对象可以被正确的初始化。

如果__new__方法不返回值（或者返回None）那么__init__将不会得到调用，因为实例都没有创建出来，调用init也没有意义
python还规定__init__只能返回None值，否则报错。

__init__可以用来做一些初始化的工作，比如给实例对象的状态进行初始化：
```python
def __init__(self,a,b):
    self.a = a
    self.b = b
    super(A,self).__init__()
```
另外，__init__方法中除了self之外定义的参数，都将与__new__方法中除了cls参数之外的
的参数保持一致或者等效
```python
class B:
    def __init__(self,*args,**kwargs):
        print("init",args,kwargs)
    def __new__(cls, *args, **kwargs):
        print("new",*args,**kwargs)
        return super().__new__(cls)
        
B(1,2,3)

#输出
new(1,2,3){}
init(1,2,3){}
```
## __new__方法
一般我们不会去重写该方法，该方法作为构造函数用于创建对象，是一个工厂函数，专用于生产
实例对象。著名的设计模式之一，单例模式，就可以通过此方法来实现。自己在写框架级代码时，可能会用到他。
微型的Web框架Bootle（https://github.com/bottlepy/bottle/blob/release-0.6/bottle.py）就可能用到
```python
class BaseController(object):
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = object.__new__(cls,*args,**kwargs)
        return cls._singleton
```
这就是通过__new__来实现单利模式的一种方式，如果实力对象存在了就直接返回该实例即可，如果没有就创建一个实例，在
返回。


## __call__方法
我们平时自定义的函数、内置函数和类都属于可调用对象（callable），但凡是可以把一对括号应用
到某个对象身上的都可以称之为可调用对象，判断对象是否为可调用对象可以用函数callable
如果在类中实现了__call__方法，那么实例对象也成为一个可调用的对象。

我们回到最开始的例子：
```python
a=A()
print(callable(a)) #True
```
a是一个实例对象，同时也是一个可调用对象，那么我们就可以像函数一样调用他：
```python
a() #__call__
```
实例对象也可像函数类作为可调用对象，这个特性在什么场景下可以用的上？
这个要结果类的特性来说，类可以记录数据（属性），而函数不行（闭包从某种意义上也行），
利用这个特性可以实现基于类的装饰器，在类里面记录状态，比如，下面这个例子用于记录函数被调用的次数：
```python
class Counter:
    def __init__(self,func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        self.count +=1
        return  self.func(*args, **kwargs)
        
@Counter
def foo():
    pass
for i in range(10):
    foo()
print(foo.count)  #10
```
```python
@Counter
def foo():
    pass
```
等价于foo = Counter(foo)
,foo这个时候就是Counter的一个实例，但是他也是可调用的，因为Class Counter定义了__call__方法,
每调用一次就会执行一次__call__方法





















