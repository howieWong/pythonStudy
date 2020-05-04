from Person import Person


class Student(Person):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)


stu = Student("jack", 19)
print(stu.name, stu.age)
