# 11.8 用selenium来控制浏览器
需要下载selenium包 pip3 install selenium
## 11.8.1 启动selenium控制的浏览器
```python
from selenium import webdriver
webdriver.Chrome().get('') #里面加入link
```
## 11.8.2 在页面中寻找元素
webdriver有很多方法在页面中寻找元素主要分为两种，find_element_*和find_elements_*方法
find_element_* 方法用于返回WebElement对象，包含页面中匹配查询的第一个元素
find_elements_* 方法用于返回WebElement对象，包含页面中所有匹配的元素

找元素的方法有很多种：
1. 通过CSS class name的元素
2. 匹配CSS selector的元素
3. 匹配id属性值的元素
4. 完全匹配提供的 text的\<a\>元素
5. 包含匹配 text的\<a\>元素
6. 匹配name属性值
7. 匹配tagname，就是html中的标签名
只有tagname这个与大小写无关，其他都是大小写严格匹配的

## 11.8.3 点击页面
WebElement对象有个方法叫做click()方法，可以点击

## 11.8.4 填写并提交表单
* 向web页面的文本字段发送点击键，只要找到那个文本字段的\<input\>或\<textarea\>元素，然后调用
send_keys()方法，里面填写的是，你需要填写在input中的内容
* 在任何元素上调用submit()方法，都等同于点击该元素在表单的Submit按钮（在gmail中没有成功，仍调用的是click方法）

## 11.8.5 发送特殊键
selenium有个模块，针对不能用字符串值输入的键盘击键，这些值保存在selenium.webdriver.common.keys模块中
这个模块名字很长，所以在程序顶部写上
```python
from selenium.webdriver.common.keys import Keys

```
原来需要写from selenium.webdriver.common.keys的地方直接用Keys就可以了
可以用send_keys()调用
```python
htmlelement.send_keys(Keys.END)
```
## 11.8.6 点击浏览器按钮
selenium可以模拟浏览器的按钮
* browser.back()    后退
* browser.forward()  前进
* browser.refresh()  刷新
* browser.quit()     退出

## 11.8.7 关于selenium更多信息
[selenium-python doc](http://selenium-python.readthedocs.org/)







##遇到报错
Q: 执行browser=webdriver.Chrome()
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs 
to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

A:
下载http://chromedriver.storage.googleapis.com/index.html?path=2.15/
下载安装包后，在一个路径下面解压，然后，将路径放入到PATH中，重启IDE然后重新执行
```python
from selenium import webdriver
browser=webdriver.Chrome()
```

Q: 遇到问题并找到解决方案 windows defender
A: https://productforums.google.com/forum/#!topic/chrome/_pTMBYdpwUE

Q:打不开网页，神烦，老是打开date页面
A:放弃chrome，
我又回来了，更新了chrome 的webdriver 问题解决，还回答了我的Stack Overflow的首个答案，现在我的chrome可以打开网页了