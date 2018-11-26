# -*- coding: utf-8 -*-
import requests, os, bs4, re, datetime,threading

today = datetime.datetime.now()
todaydate = today.strftime('%Y-%m-%d')
filetodaydate = today.strftime('%Y%m%d')

url0='http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=sgshqd&TABKEY=tab1&txtStart=%s&txtEnd=%s&random=0.9777636623336019' %(todaydate,todaydate)
url1='http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=sgshqd&TABKEY=tab1&PAGENO=2&txtStart=%s&txtEnd=%s&random=0.5149407802321062' %(todaydate,todaydate)
url2='http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=sgshqd&TABKEY=tab1&PAGENO=3&txtStart=%s&txtEnd=%s&random=0.42479184932749225' % (todaydate,todaydate)


urllist = [url0, url1,url2]
partfilepath=[]
absofilepath=[]
for useurl in urllist:
    resp = requests.get(useurl)
    jj=resp.json()
    for i in range(len(jj[0]['data'])):
        a= jj[0]['data'][i]['jjdm']
        partfilepath.append(re.findall(r'/modules.*\.txt',a))

for i in range(len(partfilepath)):
    absofilepath.append('http://www.szse.cn'+partfilepath[i][0])

textnum = [159922, 159923, 159925, 159928, 159929, 159930,
           159931, 159933, 159935, 159936, 159938, 159939,
           159940, 159944, 159945, 159946, 159951, 159953]
txtNUM=[] #txt文件在下载文件中序列号
xmlNUM=[] #xml文件在下载文件中序列号

for i in range(len(absofilepath)):
    for num in textnum:
        if str(num) in absofilepath[i]:
            txtNUM.append(i)

a=[i for i in range(54)]

def In(o):
        if o not in txtNUM:
            return True
        else:
            return False
xmlNUM=list(filter(In,a))
# print(txtNUM)
# print(xmlNUM)

downloadXmlpath=[] # 网页上取的xml下载路径['http://www.szse.cn/modules/report/views/eft_download_new.html?path=%2Ffiles%2Ftext%2FETFDown%2F&filename=pcf_159001_20181126%3B159001ETF20181126&opencode=ETF15900120181126.txt'
downloadTxtpath=[] # 网页上去的txt下载路径['http://www.szse.cn/modules/report/views/eft_download_new.html?path=%2Ffiles%2Ftext%2FETFDown%2F&filename=pcf_159922_20181126%3B159922ETF20181126&opencode=ETF15992220181126.txt',

for i in txtNUM:
    downloadTxtpath.append(absofilepath[i])
for i in xmlNUM:
    downloadXmlpath.append(absofilepath[i])
# print(downloadXmlpath)
# print(downloadTxtpath)


# 下载路径 http://reportdocs.static.szse.cn/files/text/ETFDown/pcf_159923_20181126.txt
txtfilename=[] #
xmlfilename=[]
xmlurl = []
txturl = []


for i in downloadTxtpath:
    a=re.findall(r'pcf\_\d+\_\d+',i)
    txturl.append('http://reportdocs.static.szse.cn/files/text/etfdown/'+a[0]+'.txt')
    txtfilename.append(a[0]+'.txt')
#
for xmlpath in downloadXmlpath:
    xmlpatha=re.findall(r'pcf\_\d+\_\d+',xmlpath)
    xmlurl.append('http://reportdocs.static.szse.cn/files/text/etfdown/'+xmlpatha[0]+'.xml')
    xmlfilename.append(xmlpatha[0]+'.xml')
# print(xmlurl)
# print(txturl)

def downloadtxt():
    for i in range(len(txturl)):
        reptxt=requests.get(txturl[i],timeout=500)
        reptxt.encoding='gb18030'
        reptext = reptxt.text
        with open(txtfilename[i], 'w', encoding='gb18030') as f:
            print('下载:' + txtfilename[i])
            f.write(reptext)

def downloadxml():
    for i in range(len(xmlurl)):
        reptxt=requests.get(xmlurl[i],timeout=500)
        reptxt.encoding='UTF-8'
        reptext = reptxt.text
        with open(xmlfilename[i], 'w', encoding='UTF-8') as f:
            print('下载:'+xmlfilename[i])
            f.write(reptext)


th_xml = threading.Thread(target=downloadxml)
th_txt =threading.Thread(target=downloadtxt)

th_xml.start()
th_txt.start()
th_xml.join()
th_txt.join()
print('Finish Download')