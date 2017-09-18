## 11.2.2 检查错误
```python
import requests
cont = requests.get('baidu.com')
cont.raise_for_status()  
 #对返回的对象调用raise_for_status()方法，若果下载的文件出错就会返回错误堆栈
```
