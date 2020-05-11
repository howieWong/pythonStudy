import random,math

print(random.choice([1, 2, 3, "a", 4, 5, 6]))
print(random.choice("hello world"))
print(random.choice(range(5)) + 1)#1~5
#str  = input("请输入")
#print(str)
#num = int(input("please Input  a number"))
print(random.randrange(1,100,2))#从1开始，到100结束（不包括）步长为2 ，1，3，5，7.。。。。

print( 13 % 3)#取余 1
print( 13 / 3)#除法 4.333333333
print( 13 // 3)#取整4

print(math.trunc(random.uniform(10,20)))
print(random.random())

num1 = 1
num2 = num1
print(id(num1))
print(id(1))
print(id(num2))
print(type(int(8.99)))#强转
print(type(str(8.99)))

print(2**4)#幂
print(math.pow(2,4.2))#浮点值