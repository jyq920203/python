import bs4,requests

exAmple=bs4.BeautifulSoup(open('example.html',encoding='utf-8'),"html.parser")
# 这个地方一定要加上"html.parser"，参看http://cuiqingcai.com/1319.html
# 这个地方要加上encoding='utf-8'，不然会报错不能解析，参看https://www.zhihu.com/question/22699590,
# 还有参看https://www.crifan.com/summary_python_unicodedecode_error_possible_reasons_and_solutions/


print(exAmple.select('#author'))
