import itertools
import time
import re
print(time.gmtime().tm_sec)
mylist = list(itertools.product("1234567890",repeat=5))
print(time.gmtime().tm_sec)
print(len(mylist))

print(re.match("[0-9]*[a-z]+", "1234def123",flags=re.I))
print(re.match("[0-9]*", "a123bcf"))

'''
re.match()  
re.search() 搜索整个字符串，返回第一个成功匹配的字符串
re.findall()
'''

print(re.search("www", "www.baidu.com"))
print(re.search("www", "123.www.baidu.com"))

print(re.findall("www", "www.baidu.com.www"))