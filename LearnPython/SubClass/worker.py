from Person import Person

class Worker(Person):
    def __init__(self,name,age):
        super(Worker,self).__init__(name,age)

worker = Worker("helen",20)
print(worker.name,worker.age)
worker.eat(" apple")