#格式化输出
num = 10
fnum = 1.777777779999
print("abc" in "abcde")
print("num =",num,"fnum =",fnum)
print("num = %d,\nfnum = %.3f\n"%(num,fnum))#四舍五入 去三位小数
print("num = {}， fnum = {}".format(num,fnum))
str = "0123456789"
print("tom is 'good' man ")
print("\\\\")
print(r"\\\\")# r 表示内部字符串不转义
print(r"\\\t\\\\tn]n\n\\")
print(str[6:8])# get '67'
print(str[0:3])
print(str[:3])
print(str[0:-3])#负号表示从右到左 len(str)-3
print(str[0:len(str)-3])
print("------")
print(str[-3:-2])
'''
[n:m]表示从n开始，取m-n个
[:n]表示0~n
[n:]表示n到结尾
[:-n}表示0~len(str)-n
'''

print("123" in str)#表示str是否包含 “123”， not in 不包含
print("123" not in str)

#year = int(input("input a year"))
#if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
#    print("run nian")
print("*".join("12345"))
print(None)
for row in range(1,10):
    for col in range(1,row + 1):
        print("{} * {} = {}".format(row,col,row*col),end="  ")# end = "" java print() println()
    print()

