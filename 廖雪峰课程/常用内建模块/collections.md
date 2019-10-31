# 常用的内建模块collections

##  namedtuple

namedtuple的作用是可以指定一个tuple,并且可以定义这个tuple的这个每个字段的含义，比如说我要定义一个坐标的话，我可以这么做：

```PYTHON
from collections import namedtuple
Point = collections.namedtuple('point',['x','y'])
p = Point(3,4)
p.x
p.y
```

上面的代码可以帮助我定义了一个tuple 这个，tuple 有自己的名字，定义了字段的个数，有自己每个字段的含义，这样我就不用用下标来表示我需要拿到的字段了。

上面的p 是Point的的子类，也是tuple的子类：
```PYTHON
>>> isinstance(p, Point)
True
>>> isinstance(p, tuple)
True
```
