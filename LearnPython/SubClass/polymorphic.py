class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name + " 吃东西")

class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

class Person:
    def feed(self,animal):
        print("喂食")
        animal.eat()

cat = Cat("cat")
person = Person()
person.feed(cat)


