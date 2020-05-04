class People:
    name = "class field" #class field

    def __init__(self,name,age):
        self.name = name
        self.age = age

p = People("jack",18)
print(p.name,p.age)
'''
del p.age
print(p.age)
类也没有age这个属性，删除会报错
'''
del p.name
print(p.name) #删除后会找到类属性的name
print(People.name)
