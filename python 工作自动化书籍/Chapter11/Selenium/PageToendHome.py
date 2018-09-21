#通过send_keys()来滚动页面
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
brower = webdriver.Chrome()
brower.get('http://nostarch.com')
he = brower.find_element_by_tag_name('html')
he.send_keys(Keys.END)
time.sleep(3)
he.send_keys(Keys.HOME)