class Hello:
    def sayHello(self):
        print("hello world{} {}".format(self.name,self.age))
    def __init__(self,name,age):
        self.name = name
        self.age = age

h = Hello("jack",20)
h.sayHello()


class Hi(Hello):
    def __init__(self,name,age):
        Hello.__init__(self,name,age)
    def sayHi(self):
        print("hi python")

hi = Hi("tom",11)
hi.sayHi()
