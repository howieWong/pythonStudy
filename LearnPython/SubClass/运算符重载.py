print('a' + 'b')
print(11 + 22)
print('11' + '22')


class TestOverride:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):  # 重载 重写 t1 + t2 这个方法
        return TestOverride(self.number + other.number)


t1 = TestOverride(1)
t2 = TestOverride(2)
print(t1.__class__)
print(t2)
print(t1 + t2)  ##等价与t1__add__(t2)
print(t1.__add__(t2))


