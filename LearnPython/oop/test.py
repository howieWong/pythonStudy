class A:
    def __init__(self, name):
        self.name = name
        print("create A")


class D:
    def __init__(self, title):
        self.title = title


class B(A):
    def __init__(self, name, age):
        # super(B, self).__init__(name)
        A.__init__(self, name)
        self.age = age
        print("create B")


class C(A, D):
    def __init__(self, name, age, height, title):
        super(C, self).__init__(name)
        # D.__init__(self,title)
        super(A,self).__init__(title)
        self.age = age
        self.height = height
        print("create C")

    def __str__(self):
        return "name = {},age = {},height = {},tittle = {}".format(self.name, self.age, self.height, self.title)


c = C("tome", 18, 175, "i'm D")
print(c)
