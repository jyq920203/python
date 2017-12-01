from urllib import request
response = request.urlopen(r'http://python.org/')
page = response.read()
page = page.decode('utf-8')

