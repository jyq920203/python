# 11.3 将下载的文件保存到硬盘中
***Unicode编码***

参考liaoxuefeng.com，
python3 是以unicode编码的，是支持多种语言的。
asc码是指能支持英文，只有一个字节，然后出现了unicode编码，两个字节，支持所有语言，
然后发现只处理英文的话，我们的英文处理会浪费空间出现了UTF-8编码，涉及到传输，存储计算机用的是UTF-8编码，涉及到编辑，
计算器使用的是unicode编码

* 可以使用for和iter_content()在每次循环中返回一段内容，每一段都是bytes数据类型，你需要在iter_content()中指定包含多少
字节，10w字节通常是个不错的选择
```python
import requests
file = open('filename','wb')
res = requests.get('http://baidu.com')
for contentIter in res.iter_content():
    file.write(contentIter)
    
file.close()  
```