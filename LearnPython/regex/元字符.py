import re
'''
(xyz)
x? 0个或1个，非贪婪，尽可能少 *? +?
(?:x) something like (xyz)
x* 0个或多个，贪婪，尽可能多
x+ 1个或多个，贪婪，尽可能多
x{n} n个x
x{n,} 至少n个x
x{n,m} 至少n个至多m个x，n<=m
x|y 匹配x或者y
'''

print(re.findall(r"a?","aaa"))
print(re.findall(r"a*", "aaabaa"))
print(re.findall(r"a+", "aaabaa"))
print(re.findall(r"a{3}", "aaabaa"))
print(re.findall(r"a{3,}", "aabaaacaaaa"))
print(re.findall(r"a{3,5}", "aabaaacaaaa"))
print(re.findall(r"(ab|ba)", "aabbccbbaa"))
print(re.findall(r"((t|T)om)", "tom-Tom"))
str="tom is a good man. tom is a nice man"
print(re.findall(r"^tom.*man$",str))
print(re.findall(r"tom.*?man",str))
### non-greedy match  ?
str= "/* part1 */   /* part2 */"
print(re.findall(r"/\*.*\*/",str))
print(re.findall(r"/\*.*?\*/",str))

regex = r"(1([3578]\d|47)\d{8})"
print(re.findall(regex,"15620934152abc15620934152cdde1385125907914722233369"))