set = {1,2,3,4,555,6,55,6,6,9}
'''
无序
无重复
'''
print(set)

set.add(10)
print(set)
set.update([1,2,3,4,5])
print(set)

s = iter(set)
while True:
    try:
        print(next(s))
    except StopIteration:
        print("over")
        break

