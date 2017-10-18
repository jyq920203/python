## Python中staticmethod方法和classmethod方法区别
参考：http://www.firefoxbug.com/index.php/archives/2818/
这篇文章区分了静态方法和类方法的定义上的差异，类方法第一个参数是cls，静态方法是不存在任何与类、实例
相关的参数。
讲述了使用场景：
python本身不支持函数的重载（顶多支持函数的取代。。。）但是classmethod可以实现类似重载的功能
重载是参数变化，但是函数名称不变，重写是子类继承父类方法，函数的名字，参数都不变当时具体实现逻辑变化
静态方法一般用于跟类有关系的功能，但是运行时又不需要实例可类参与的情况
比如更改环境变量或者其他类的属性等能用到的静态方法。

# 如何在Python中使用static、class、abstract方法（权威指南）
参考：http://python.jobbole.com/81595/
https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
这篇简直完美！！！重点阅读！！！
讲解了为什么要使用静态方法和类方法，中文翻译的不是很好，回头在看下英文版的
https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods



## Python的静态方法和类成员方法
参考http://www.cnblogs.com/2gua/archive/2012/09/03/2668125.html
这篇也很经典！！！，讲述了静态方法类方法关于对类属性和实例属性的访问权限
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

## 实例方法、类方法和静态方法
参考：http://www.cnblogs.com/qiaojushuang/p/6403371.html
这篇文章很棒，讲解了三者的区别，还有使用类方法和静态方法有什么好处
总结：静态方法大概只是为了代码更好的组织，其实跟类类的属性，都没啥关系，但是调用的时候，要用
实例或者类来调用，在子类中可以继承静态方法，但是不能修改。
类方法传入的第一个参数就是cls，就是类本身，如果子类继承父类，子类会拥有父类的类方法，并且这个方法会
自动指向子类本身，这个特性在工厂函数中很有用。

# Python 中的 classmethod 和 staticmethod 有什么具体用途？
参考：https://www.zhihu.com/question/20021164