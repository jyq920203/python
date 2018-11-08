## 计算属性

[计算属性连接](https://woodpecker.org.cn/diveintopython3/special-method-names.html#basics)

|序号|目的|所编写的代码|python实际调用|
|---|---|---|---|
|1|获取一个计算属性（无条件）|`x.my_property`|`x.__getattribute__(my_property)`|
|2|获取一个计算属性（后备）|`x.my_property`|`x.__getattr__(my_property)`|
|3|设置某属性|`x.my_property = value`|`x.__setattr__('my_property',value)`|
|4|删除某属性|`del x.my_property`|`x.__delattr__('my_property')`|
|5|列出所有属性和方法|`dir(x)`|`x.__dir__()`|


### 同时定义


```python
class Dynamo:
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


dyn = Dynamo()
print(dyn.color)
print(dir(dyn))
dyn.color = 'ihao'
print(dyn.color)
print(dir(dyn))
```
结果展示：
```python
PapayWhip
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__return__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
ihao
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__return__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color']
```
说明下这个例子：
1. `dyn.color` 获取某一个计算属性，执行的是`__getattr__(self, key)`,所以dyn.color='color',但是这个时候，dir（dyn）看到的属性中并没有添加color
2. 手工指定`dyn.color = 'ihao'`的时候，这个时候的dir（dyn）才会添加color这个属性。
3. 当实例有了这个color属性之后，那么访问这个color属性的时候就不需要通过`__getattr__`方法，直接返回属性值。

我们再看下`__getattribute__`方法,
```python
class Dynamo:
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


dyn = Dynamo()
print(dyn.color)
dyn.color = 'ihao'
print(dyn.color)

```
结果返回：
```python
PapayaWhip
PapayaWhip
```
说明下这个案例：
1. `print(dyn.color)` 跟上面一样，想要访问这个实例的属性，那么就要调用`__getattribute__`方法，返回了PapayaWhip，但是实例没有属性color
2. `dyn.color = 'ihao'` 使得实例拥有了属性color，并获得值是ihao
3. `print(dyn.color)` 为什么没有返回ihao呢，这个是`__getattribute__`跟`__getattr__`的区别。`__getattr__`在当实例有这个属性的时候就不执行了，程序会直接返回这个实例的属性值，但是`__getattribute__`是无条件一定会执行的，当你需要访问属性或者方法的时候，当`__getattribute__`再次执行的时候，那么返回的就还是PapayaWhip。


这个时候我们再来看下上面那个表中每一行的注释：
1. 如果某个类定义了`__getattribute__`方法，那么在每次引用属性或者方法名称的时候，都会调用它（特殊方法名称除外，因为会导致无限循环）
2. 如果某个类定义了`__getattr__`方法，python只有在正常的位置查询的时候才会调用它，如果实例x定义了属性color，那么x.color将不会调用`x.__getattr__('color')`,只会返回x.color已经定义好的值。
3. 无论何时给属性赋值，都会调用`__setattr__`方法
4. 无论何时删除一个属性，都会调用`__delattr__`方法
5. 如果定义了`__getattr__`或者`__getattribute___`方法，`__dir__`方法都会很有用，通常，调用dir(x)将只显示正常的属性和方法，如果`__getattr__`方法动态处理color属性，dir(x)将不会将color列为可用属性。可通过覆盖`__dir__`方法将color列为可用属性，对于想使用你的类但是不想深入其内部来说，该方法非常有益。


在举两个例子对比下：
```python
class Dynamo:
    def __init__(self,color):
        self.color = color
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


dyn = Dynamo('black')
print(dyn.color)
```
结果返回的是： 
```python
'PapayaWhip'
```

执行顺序是：
1. dyn = Dynamo('black') 这句首先会执行`__init__`方法进行实例的初始化
3. print(dyn.color) 这句因为会访问dyn的属性color，而且定义了`__getattribute__`这个获取属性获得方法一定会执行的语句，结果就返回了PapayWhip。

但是如果同样的语句，但是里面使用的是`__getattr__`方法，那么返回的就是black了，因为当实例有了color属性后，访问该属性，就会直接返回该属性的值，而不是调用`__getattr__`方法。
```python
class Dynamo:
    def __init__(self,color):
        self.color = color
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


dyn = Dynamo('black')
print(dyn.color)
```

当`__getattr__`和`__getattribute__`同时存在时候，下面的程序返回的结果跟第一次一样，返回的是PapayaWhip,因为会执行`__getattribute__`语句，但是不会执行`__getattr__`语句。
```python
class Dynamo:
    def __init__(self,color):
        self.color = color
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

dyn = Dynamo('black')
print(dyn.color)

```


