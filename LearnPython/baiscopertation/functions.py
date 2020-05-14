def sum(a, b):
    return a + b


print(sum(1, 2))
list = [1, 2, 3, 4, 5, 6]


def change(list):
    list[-1] = -1


change(list)
print(list)
'''
关键字参数
默认参数
'''


def printdd(name="jack", age=22):
    print(name, age)


printdd(age=18, name="tom")
printdd()
printdd("helen")
printdd(age=11)

'''
可变参数 *args，**kargs
'''


def name(*args):
    # print(type(args))
    if len(args) == 0:
        print("none")
    else:
        print(args)


name()
name("a", 'b', 'c')


def name2(**kwargs):
    print(type(kwargs))
    print(kwargs)


name2()
name2(name="tome", age=18, country='China')


def anyparameter(*args, **kwargs):
    printdd(args, kwargs)


anyparameter(1, 2, 3, 4, age=18)

'''
匿名函数 不使用def定义
使用lambda表达式实现简单的逻辑
自能使用自己命名空间的变量
lambda 参数1，参数2.。。参数n:
    expression
'''
ex1 = lambda a, b: print(a,b)
ex1(1,2)