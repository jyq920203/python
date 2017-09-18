# 要做的事情：
# 1.登陆到xkcd网页中，找到页面中图片的标签，下载下来
# 2.然后获取prev的link，然后重复
# 3.直到网页地址是以#号结尾的，因为这是第一张

import requests,bs4,os
url='http://www.xkcd.com'
content = requests.get(url)
beautifulSoup = bs4.BeautifulSoup(content.text, "html.parser")
# print(beautifulSoup.select('#comic img')[0].get('src'))
urlname = beautifulSoup.select('#comic img')[0].get('src')

os.mkdir()
imgfile = open(os.path.join(urlname.basename),'wb')




#出现过错误，
# 1.错误是BeautifulSoup没有使用"html.parser"
#2.url没有加http开头

#img 标签
#alt 和src标签是两个必要的标签，alt规定了图像的替代文本，src规定了显示图像的url

#实在找不到这个标签和其他标签有什么不同的时候就用id标签来寻找

#207页，章节中的创建文件目录不会使用函数makedir，查看第八章节，笔记记录在Chapter 8中