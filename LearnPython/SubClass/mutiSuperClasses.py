class Person:
    def __init__(self, intelligence):
        self.intelligence = intelligence

    def basic(self):
        print("basic functionality of person")


class Father(Person):
    def __init__(self, familyName, money, intelligence):
        Person.__init__(self, intelligence)
        self.familyName = familyName
        self.money = money

    def play(self):
        print("father play")

class Mather:
    def __init__(self, faceValue):
        self.faceValue = faceValue


class Child(Father, Mather):
    def __init__(self, familyName, money, faceValue, name, intelligence):
        #Person.__init__(self, intelligence)
        Father.__init__(self, familyName, money, intelligence)
        Mather.__init__(self, faceValue)
        self.name = name

    def myname(self):
        print(self.name)

    def play(self):
        print("child play")


# def main():
c = Child("abc", 11, 22, "jack", 300)
c.myname()
c.basic()
c.play()

# if __name__ == "main":
#    main()
