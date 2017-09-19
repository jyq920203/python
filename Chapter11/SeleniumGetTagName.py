#获取bookcover的tagname
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')
try:
    elemen= browser.find_element_by_class_name('bookcover')
    print(elemen.tag_name)
except:
    print('no name here.')