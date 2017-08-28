import requests,bs4,webbrowser
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
Answer = input('What do you want to search?')
print('googling......')
# print('http://google.com/search?q='+Answer)
# webbrowser.open('http://google.com/search?q='+Answer)
# res = requests.get('http://google.com/')
# res.raise_for_status()

webbrowser.open('http://baidu.com/s?wd='+Answer)
res = requests.get('http://baidu.com/s?wd='+Answer)
print(res.text)
res.raise_for_status()

# search?q='+Answer,headers={'Connection':'close}

#todo requests.get怎么走代理