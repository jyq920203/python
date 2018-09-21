import re,bs4,requests,json,datetime,os

todaydate = datetime.datetime.now()
strData = todaydate.strftime('%m%d')

basicUrl = 'http://query.sse.com.cn/infodisplay/queryETFNewAllInfo.do?type='
urldanshichang = basicUrl+'1'
urlkuashichang = basicUrl+'2'
urlkuajing = basicUrl+'3'
urlhuobi = basicUrl+'4'
urlzhaiquan = basicUrl+'5'
urlhuangjin = basicUrl+'6'
#单市场ETF
danshichangfile = []
danshichangdownloadUrl = []
#跨市场ETF
kuashichangfile = []
kuashichangdownloadUrl = []
#跨境ETF
kuajingfile = []
kuajingdownloadUrl = []
#债券ETF
zhaiquanfile = []
zhaiquandownloadUrl = []
#黄金ETF
huangjinfile =[]
huangjindownloadUrl = []
#货币ETF
huobifile =[]
huobidownloadUrl = []

ETFURLdict={'urldanshichang':urldanshichang,'urlkuashichang':urlkuashichang,'urlkuajing':urlkuajing,'urlzhaiquan':urlzhaiquan,'urlhuangjin':urlhuangjin,'urlhuobi':urlhuobi}

def download(type,file=[],downloadUrl=[]):
    reqheader = {'Referer':'http://www.sse.com.cn/disclosure/fund/etflist/'}
    rep = requests.get(ETFURLdict[reqURL], headers=reqheader, timeout=500)
    rep.encoding = 'UTF-8'
    os.makedirs('./' + type,exist_ok=True)
    openfile = open('./' + type + '/' + type + '.txt','w')
    openfile.write(rep.text)
    openfile.close()

    with open('./' + type + '/' + type + '.txt','r') as jsonfile:
        data = json.load(jsonfile)

    for i in range(len(data['pageHelp']['data'])):
        file.append(data['pageHelp']['data'][i]['fundid1'] + strData + '.ETF')  # ['etfFullName']
        downloadUrl.append("http://query.sse.com.cn/etfDownload/downloadETF2Bulletin.do?etfType=" + data['pageHelp']['data'][i]['etftype'])
    for j in range(len(file)):
        rep = requests.get(downloadUrl[j], timeout=500)
        rep.encoding = 'gb18030'
        downloadfile = open('./'+ type + '/' + file[j], 'w', encoding='gb18030')
        downloadfile.write(rep.text)
        downloadfile.close()

    

for reqURL in ETFURLdict:
    if reqURL == 'urldanshichang':
        download('danshichang',danshichangfile,danshichangdownloadUrl)              
    elif reqURL == 'urlkuashichang':
        download('kuashichang',kuashichangfile,kuashichangdownloadUrl)   
    elif reqURL == 'urlkuajing':
        download('kuajing',kuajingfile,kuajingdownloadUrl)   
    elif reqURL == 'urlzhaiquan':
        download('zhaiquan',zhaiquanfile,zhaiquandownloadUrl) 
    elif reqURL == 'urlhuangjin':
        download('huangjin',huangjinfile,huangjindownloadUrl) 
    elif reqURL == 'urlhuobi':
        download('huobi',huobifile,huobidownloadUrl) 


















#todo
# 最后一个的名字不是序号
# 上海下载的文件最后是0结尾不是显示的1结尾5106500522.ETF







# print(rep.text)
# beauty = bs4.BeautifulSoup(rep.text,"html.parser")
# print(beauty.select('.table'))


# 思路
#先http://query.sse.com.cn/infodisplay/queryETFNewAllInfo.do?type=1获取到etftype，下载路径就是用的这个etftype