def outer2(fun1):
    def inner():
        print("*"*20)
        fun1()
    return inner

'''
表示用outer2装饰fun1
不用执行fun = outer2(fun1)
fun()
'''
@outer2
def fun1():
    print("hello world")
'''
inner 表示方法
inner（） 表示执行方法
'''
fun1()
#fun = outer2(fun1)
#fun()


def outerpeople(people):#传入方法名
    def inner(name,age):
        if not name:
            name = "Python"
        if age < 0:
            age =-age
        people(name,age)
    return inner

''' @outerpeople 传入方法名，不是调用方法outerpeople()'''
@outerpeople
def people(name,age):
    print("%s is %d years old."%(name,age))
'''传入方法名，这时候返回的是f=inner'''
f = outerpeople(people)
'''调用方法的时候要加参数，这是调用的是f(None,-1)其实调用的是inner(name,age)'''
f(None,-1)
people("jack",-22)


def foo(foo1):
    def inner(*args,**kwargs):
        print("excute a**b")
        foo1(*args,**kwargs)
    return inner

@foo
def foo1(a,b):
    print(a**b)

foo1(2,3)
