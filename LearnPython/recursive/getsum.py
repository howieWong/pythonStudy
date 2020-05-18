def getSum(n):
    if n == 1:
        return 1
    return getSum(n - 1) +  n

print(getSum(10))

import os

def printDir(file):
    pass

stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack)