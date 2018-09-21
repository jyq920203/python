#版本1：
#程序到了sap()调用的时候就直接奔溃了，打出反向调用的错误栈并不会执行到print('hello')
def sap():
    hub()
def hub():
    raise Exception('an error')
sap()
print('hello')



#版本2：
#如果你不使用try...except...来包围的话，就会打出错误堆栈，如果处理了就不会打出错误堆栈
#如果使用try...catch...包围的话，有异常就会跑到Except中，
#程序不会崩溃,而且会继续执行之后的语句
def sap():
    hub()
def hub():
    raise Exception('an error')

try:
    sap()
except:
    print('happy')
    
print('sad')



#版本3
#如果try语句中没有出现异常，那么是不会出执行except中的语句的
try:
    print('hellox')
except:
    print('happy')




