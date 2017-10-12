# 要做的事情：
# Chapter1.登陆到xkcd网页中，找到页面中图片的标签，下载下来
# 2.然后获取prev的link，然后重复
# 3.直到网页地址是以#号结尾的，因为这是第一张

import requests,bs4,os
url='http://www.xkcd.com'
os.makedirs('.'+os.path.sep+'xkcd',exist_ok=True)
while not url.endswith('#'):
    print(url)
    print('Downloading page %s...' %url)
    content = requests.get(url)
    beautifulSoup = bs4.BeautifulSoup(content.text, "html.parser")
    # print(beautifulSoup.select('#comic img')[0].get('src'))
    urlname = 'http:'+ beautifulSoup.select('#comic img')[0].get('src')
    print('Downloading image %s...' %urlname)
    previPage =beautifulSoup.select('a[rel="prev"]')[0].get('href')
    res = requests.get(urlname)


    for imgcontent in res.iter_content(100000):
        imgfile = open(os.path.join('xkcd', os.path.basename(urlname)), 'wb')
        imgfile.write(imgcontent)
        url = 'https://xkcd.com/' + previPage
    imgfile.close()






#出现过错误，
# Chapter1.错误是BeautifulSoup没有使用"html.parser"
#2.url没有加http开头

#img 标签
#alt 和src标签是两个必要的标签，alt规定了图像的替代文本，src规定了显示图像的url

#实在找不到这个标签和其他标签有什么不同的时候就用id标签来寻找

