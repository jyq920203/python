# -*- coding: utf-8 -*-
import requests, os, bs4, re, datetime,threading

today = datetime.datetime.now()
todaydate = today.strftime('%Y-%m-%d')
filetodaydate = today.strftime('%Y%m%d')


url = 'http://www.szse.cn/szseWeb/FrontController.szse?randnum=0.7266794520575823&ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=sgshqd&TABKEY=tab1&REPORT_ACTION=search&txtStart=%s&txtEnd=%s' % (todaydate, todaydate)
url1 = 'http://www.szse.cn/szseWeb/FrontController.szse?randnum=0.7266794520575823&ACTIONID=7&AJAX=AJAX-TRUE&CATALOGID=sgshqd&TABKEY=tab1&txtStart=%s&txtEnd=%s&tab1PAGENO=2&tab1PAGECOUNT=2&tab1RECORDCOUNT=54&REPORT_ACTION=navigate' % (todaydate, todaydate)


urllist = [url, url1]
finallist = ""
for num in range(len(urllist)):
    rep = requests.get(urllist[num],timeout = 500)
    textfile = open('a.html', 'wb')
    for textCha in rep.iter_content(100000):
        textfile.write(textCha)
    textfile.close()
    beauty = bs4.BeautifulSoup(rep.text, "html.parser")
    for i in range(len(beauty.select('span[style="cursor:pointer"]'))):
        ha = beauty.select('span[style="cursor:pointer"]')[i]
        finallist = finallist + ha.get('onclick')
        # 获取到onclick的属性值放到 finallist中

matchline = re.findall(r'pcf\_\d+\_\d+', finallist)
# matchline中放置文件名称，是一个列表，是所有的文件的名字
# print(matchline)

txtdownloadurl = []
xmldownloadurl = []
textfilename = []
xmlfilename = []
finaltextname = []
textfilelist = []
xmlfilelist = []

textnum = [159922, 159923, 159925, 159928, 159929, 159930, 159931, 159933, 159935, 159936, 159938, 159939, 159940,
           159944, 159945, 159946, 159951,159953]
#txt 的ETF
for numtext in textnum:
    finaltextname.append('pcf_' + str(numtext) + '_' + filetodaydate)
# 将txt文件的凑成文件名字放到finaltextname列表中

for name in matchline:
    if name in finaltextname:
        textfilelist.append(name)
        for url in textfilelist:
            txtdownloadurl.append('http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=downloadEtf&filename=' + url)
            textfilename.append(url + '.txt')

    if name not in finaltextname:
        xmlfilelist.append(name)
        for url in xmlfilelist:
            xmldownloadurl.append('http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=downloadEtf&filename=' + url)
            xmlfilename.append(url + '.xml')

def downloadtxt():
    for i in range(len(txtdownloadurl)):
        reptxt = requests.get(txtdownloadurl[i],timeout = 500)
        reptxt.encoding = 'gb18030'
        reptext = reptxt.text
        xmlfile = open(textfilename[i], 'w', encoding='gb18030')
        xmlfile.write(reptext)
        xmlfile.close()

def downloadxml():
    for i in range(len(xmldownloadurl)):
        rep = requests.get(xmldownloadurl[i],timeout = 500)
        rep.encoding = 'UTF-8'
        reptext = rep.text
        xmlfile = open(xmlfilename[i], 'w', encoding='UTF-8')
        xmlfile.write(reptext)
        xmlfile.close()


th_xml = threading.Thread(target=downloadxml)
th_txt =threading.Thread(target=downloadtxt)

th_xml.start()
th_txt.start()
th_xml.join()
th_txt.join()
print('Finish Download')






