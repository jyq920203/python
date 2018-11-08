## 计算属性

[计算属性连接](https://woodpecker.org.cn/diveintopython3/special-method-names.html#basics)

|序号|目的|所编写的代码|python实际调用|
|---|---|---|---|
|1|获取一个计算属性（无条件）|`x.my_property`|`x.__getattribute__(my_property)`|
|2|获取一个计算属性（后备）|`x.my_property`|`x.__getattr__(my_property)`|
|3|设置某属性|`x.my_property = value`|`x.__setattr__('my_property',value)`|
|4|删除某属性|`del x.my_property`|`x.__delattr__('my_property')`|
|5|列出所有属性和方法|`dir(x)`|`x.__dir__()`|

1. 如果定义了`__getattribute__()`方法


### 同时定义


print(dir(dyn))
dyn.color = 'LemonChiffon'
print(dir(dyn))



   def __getattribute__(self, key):
        if key == 'color':    
            return 'PapayaWhip'
        else:
            raise AttributeError 