#功能：打开inventwithpython页面，点击Read It Online 的链接
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://www.inventwithpython.com')
linkElem=browser.find_element_by_link_text('Read It Online')
linkElem.click()

#这边要注意的事情是，从linktext获取到webElement，必须要注意到大小写