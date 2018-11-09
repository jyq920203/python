## dict

删除一个key，使用pop(key)方法，对应的value也会从dict中删除：
```python
b={'Michael': 95, 'Tracy': 85,'nihao':88}
b.pop('Michael','Tracy')
95
b
{'Tracy': 85, 'nihao': 88}
```
而且注意到，删除的value还会作为函数的返回体返回。