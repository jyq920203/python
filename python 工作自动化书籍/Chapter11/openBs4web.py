import bs4,requests
getWeb=requests.get('http://cuiqingcai.com/1319.html')
getWeb.raise_for_status()
WebElems=bs4.BeautifulSoup(getWeb.text,"html.parser")
print('--------------------------')
print(WebElems.select('.blogroll'))

print(len(WebElems))

# <ul class="xoxo blogroll"> 遇到这种里面有空格的，在做class选择器的时候可以只选一部分，可以使用
#.blogroll或者.xoxo或者.xoxo.blogroll
# 参看https://zhidao.baidu.com/question/311666643.html
#-------------------------------------------------------
# 关于ol，li，ul
# http://www.runoob.com/tags/tag-ul.html
# ul可以创建无序列表，经常跟li一起使用；ol是创建有序列表


