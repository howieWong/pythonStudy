import re
'''
 . 匹配除换行符以外的所有字符 
 [0123456789] 匹配某一个数字
 [0-9a-zA-Z]
 [howie]匹配h o w i e 任意一个字符
 [^abc] 除abc以为的所有字符  ^脱字符
 \d 匹配数字[0-9] \D 匹配非数字[^0-9]
 \w 匹配数字字母下划线[0-9a-zA-Z_]
 \W 匹配非数字字母和下划线[^0-9a-zA-Z_]
 \s [ \f\n\r\t] 所有空白字符 空格换行回车制表符等
 \S [^ \f\n\r\t]
 \b 单词边界 单词和空格位置 today is a good day
 \B 非单词边界
'''

print(re.search(".", "howie"))
print(re.search("[howie]","abcde"))
print(re.search("[0-9a-z]*", "howieH",flags=re.I))
print(re.search("[^a-z]", "abcd123"))
print(re.search(r"abc\d","abc123"))
print(re.search("\D","abc123"))
print(re.search("\w", "_abc123"))
print(re.search("\s", " abc"))
print(re.findall("\D","i'm 18 \n ears 9"))
print(re.findall("\Aab", "ab\nab",re.M))#只匹配第一个行首
print(re.findall("^ab", "ab\nab",re.M))
print(re.findall("ab\Z", "ab\nab",re.M))#只匹配第一个行尾
print(re.findall("ab$", "ab\nab",re.M))
print(re.search("today\\b","today is a good day"))
