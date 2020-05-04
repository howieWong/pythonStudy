class Person:
    # __slots__ = ("name", "age","id")  ## 限制添加属性

    def __init__(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id


per = Person(100)
# AttributeError: 'Person' object has no attribute 'height'
# per.height = 100
print(per.getId())
per.setId(101)
print(per.getId())


class People:
    def __init__(self, id):
        self.__id = id

    # @property

    @property# 代替get方法
    def id(self):
        return self.__id

    @id.setter#代替set方法，@[field].setter
    def id(self, id):
        self.__id = id


peo = People(200)
print(peo.id)
peo.id =201
print(peo.id)
