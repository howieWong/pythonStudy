class Person(object):
    __hobby = "xxx" #private
    _family = "guannan" # regard as a private field 

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.__weight = weight

    #  def __init__(self, name, salary):
    #     self.name = name
    #      self.__salary = salary #private field

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight < 0:
            weight = 0
        print(self.__hobby)
        self.__weight = weight

    def __str__(self):  # when printing an object such as print(obj) and then invoke this method
        # return self.name + str(self.age) + str(self.height) + str(self.weight)
        return "name={},age={},height={},weight={}".format(self.name, self.age, self.height, self.__weight)


per = Person("jack", 20, 177, 61)
print(per)
print(per.getWeight())
per.setWeight(90)
print(per.getWeight())
per.setWeight(-5)
print(per.getWeight())
print(per._family)
