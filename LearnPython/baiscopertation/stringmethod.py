#eval(str)
print(eval("123,str"))
print(eval("False and True"))
print(eval("3**4"))
str="hello world world WORLDw"
print(str.lower())
print(str.upper())
print(len(str))
print(type(str))
print(str.swapcase())
print(str.capitalize())
print(str.title())#单词首字母大写
print(str.count("L"))#返回L的个数
print(str.rfind("w"))#最后一个w
print(str.find("w"))#第一个w
s1= "   str8888  str     "#strip()截取两侧的空格，可以指定
print(s1.lstrip())
s2="***str888str****"
print(s2.rstrip(("*")))
print(ord('a'))
print(ord("A"))
print(ord("b")-ord("a"))
print(chr(65))
ceshi = "对影成三人"
a1 = "*".join(ceshi)
print(a1)