import re
'''
compile
1 check syntax
2 match object with a compiling regular expression
compile(pattern,flags=0)
pattern: the regular expression to be compiled
'''
pat = r"^1(([3578]\d)|(47))\d{8}$"
re_pat = re.compile(pat)## pattern object
print(re_pat.match("15620934152"))

re_QQ= re.compile(r"^[0-9]\d{5,9}$")
print(re_QQ.search("014642365"))

'''
group  ()
extract substring

(?P<"NAME">) give a name to a group
'''
s = "010-53256845"
#m = re.match(r"(\d{3})-(\d{8})",s)
m = re.match(r"(?P<first>\d{3})-(\d{8})",s)
print(m)
#print(type(m))
print(m.group("first"))
#print(m.groups())
print(m.group(1))
print(m.group(2))
str1 = " tom   is good man"
print(str1.split(" "))
print(re.split(r" +", str1))
print(str1[0:4])

i = re.finditer(r"(tom)", "tom is good man, tom is nice man, tom is bright man")
while True:
    try:
        print(next(i))
    except StopIteration as e:
        break
'''
try:
    ...
except Exception as e:
    ...
'''


#replacement and modification of string


#str1 = " tom is good good good man"
#print(re.sub("good","nice",str1,count=1))
#print(type(re.sub("good", "nice", str1, count=1)))

