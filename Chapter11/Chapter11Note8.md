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
















##遇到报错
Q: 执行browser=webdriver.Chrome()
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

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