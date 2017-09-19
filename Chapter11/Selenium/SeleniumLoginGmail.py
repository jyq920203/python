from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://www.gmail.com')
EmailElem=browser.find_element_by_id('identifierId')
EmailElem.send_keys('jyq920203@gmail.com')
NextElem = browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
NextElem.click()
time.sleep(2)

passWdElem = browser.find_element_by_name('password')
print('dinf')
passWdElem.send_keys('Jyq@920203')
PassNextElem = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
PassNextElem.click()



#todo
# 在找passWdElem = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
# 通过xpath找不到元素
# http://www.jianshu.com/p/89c10770d72c
# http://www.cnblogs.com/alwayswyy/p/4988545.html
# http://www.51testing.com/html/87/300987-831171.html
# http://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
# https://testerhome.com/topics/7359   等待时间

#todo
看下howtofindyourwebelements中的todo


#todo
# 1. 跟之前获取元素CSS选择器做对比
# 2. 了解下
#
#
# ```html
#
# ```
#
#
# <input type="password" class="whsOnd zHQkBf" jsname="YPqjbf"
# autocomplete="current-password" spellcheck="false" tabindex="0" aria-label="输入您的密码"
# name="password" autocapitalize="off" autocorrect="off" dir="ltr"
# data-initial-dir="ltr" data-initial-value="">
