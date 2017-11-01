# 使用__slots__方法
定义一个类之后，可以给这个类动态绑定方法和属性，这就是动态语言的灵活性
## class 可以动态绑定属性

```python
class Student(object):
    pass
>>> a=Student()
>>> a.happy='happy'
>>> a.happy
'happy'
```

## class 可以动态绑定一个方法

利用types中的MethodTypes可以将方法动态的绑定到实例上，不过要注意的是，绑定到一个实例上只能在本实例中生效，
对于从属于同一个类的不同实例是不生效的。

```python
def sad(self,value):
    self.sad = value
    
>>> from types import MethodType
>>> a.sad = MethodType(sad,a)
>>> a.sad('hapy')
>>> a.sad
hapy

```
注意下语法：
1. 想要绑定方法的话，要from types import MethodTypes
2. 然后要用实例.方法名 = MethodTypes(方法名，实例名)


## 给类绑定方法
要注意的是，我们给实例绑定的方法，另一个该类的实例是不拥有该方法的，所以为了使所有的类都有该方法的话，就要用给类绑定这样的方法。
```python
class Student(object):
    pass

def haha(self,value):
    self.age = value
    
Student.haha = haha

>>> s1 = Student()
>>> s2 = Student()

>>> s1.haha(35)
>>> s1.age
35
>>> s2.haha(40)
>>>s2.age
40


```

## __slots__参数可以动态绑定指定的参数
动态语言可以任意绑定属性，如果想要实例限制绑定的属性，就要用到__slots__这个属性值
千万注意：这边说的是限制实例的属性，不是说限制类的属性，类还是可以绑定属性的。
```python
class Student(object):
    __slots__ = ('name','age')

>>> a.age =23
>>> a.age
23

>>> a= Student()
>>> a.niubia = 'haha'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'niubia'
```
## slots对于类的实例是没有效果的
也就是说如果一个类设置了slots，然后有个子类是继承于刚才的类，这个子类的实例是不受到父类的限制的，只有对当前类的实例才有作用。
除非你对子类也实现了slots，那么子类的限制的slots就是父类的加上子类的，只能从这里面选添加需要绑定的参数。
```python
class son(Student):
    pass
    
>>> s1= son()
>>> s1.heihei = '90'
>>> s1.heihei
'90'
```



