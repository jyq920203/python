# 8.1 文件与文件路径

## 8.1.1 windows上的反斜杠和类linux上的正斜杠
* windows上使用的是反斜杠\，linux类系统使用的是正斜杠/
* os.path.join('happy','sad')  在windows上返回的是'happy\\sad',其中一个反斜杠用来做转义，
注意在单引号引用中，我们使用的都要是经过转义的就是需要反斜杠就必须要用两个

## 8.1.2 当前工作目录
* os.getcwd()可以获取当前工作目录
* os.chdir('')来改变当前工作位置的路径，相当于linux中的cd命令，注意单引号中在window系统中要用两个反斜杠

## 8.1.4 用makedirs()创建新文件夹

```python
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
#walnut 核桃
#waffles 华夫饼
```
## 8.1.5 os.path 模块
这个模块包含了很多文件名和文件路径有用的函数
os.path.join()可以来构建在所有操作系统中都有效的路径
os.path 是os模块中的，所有只要import os就可以了

## 8.1.6 处理绝对路径和相对路径
```python
import os
os.path.abspath('') #返回对应的绝对路径
os.path.isabs('') #查看当前路径是不是绝对路径
os.path.relpath(path,start) #返回从start路径到path路径的相对路径的字符串
os.path.dirname(path)  #返回路径最后一个斜杠之前的所有内容  目录名称
os.path.basename(path) #返回路径最后一个斜杠之后的所有内容  基本名称
os.path.split(path)  #得到将path中的basename和dirname分开，并组成这两个字符串的元组
yourdir.split(os.path.sep) #os.path.sep可以获取当前系统的路径分隔符，
# 然后将前面的字符串按照这个字符进行分割，返回的是每个部分的列表
```
## 8.1.7 查看文件的大小
```python
import os
os.path.getsize(filename)  #显示文件大小
os.listdir(path)   #显示path目录下有哪些文件
```
## 8.1.8 检查文件的有效性
```python
import os
os.path.isdir(path)   #查看path是不是一个路径
os.path.isfile(path)  #查看path是不是一个文件
os.path.exists(path)  #查看路径是否存在
```