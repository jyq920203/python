# 写代码的时候遇到很有意思的一个问题，就是在我使用property的时候，我定义的方法跟我的属性名称不一致，结果debug的时候，多出来一个属性
class A:
    pramA=""
    pramB=""

    @property
    def pramA(self):
        return self.pramA
    @pramA.setter
    def pramA(self,value):
        self.pramA=value

a=A()
a.pramA = "b"