import requests,bs4,webbrowser
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
Answer = input('What do you want to search?')
print('baiduing......')
# print('http://google.com/search?q='+Answer)
# webbrowser.open('http://google.com/search?q='+Answer)
# res = requests.get('http://google.com/')
# res.raise_for_status()
#todo requests.get怎么走代理,如果要使用谷歌的话
# search?q='+Answer,headers={'Connection':'close}


#webbrowser.open('http://baidu.com/s?wd='+Answer)
res = requests.get('http://baidu.com/s?wd='+Answer)
#print(res.text)
res.raise_for_status()
SOUP=bs4.BeautifulSoup(res.text,"html.parser")
#记住加上(,"html.parser")
#print(SOUP.select('div h3 a'))
#select('div h3 a')找到的是div 下h3 下的a
happNum=min(len(SOUP.select('div h3 a[href]')),5)




for i in range(happNum):
    print(SOUP.select('div h3 a')[i].get('href'))

#获取链接的属性值使用的是get('属性名称')





