a = 35
res=[]
for i in range(2,a):
    if a % i == 0:
        res.append(i)
        a //= i
    else:
        pass
print(res)

list1 = []
print(list1 == None)
list1=[1,2,'a',"str","str",True]
print(list1.__len__())
print(len(list1))
print( 1 in list1)
print(list1.count("str"))
#增删改查  append(将添加的元素作为整体) extend(将添加的元素拆开)
print(id(list1))
list1.append(["a",'b','c'])
print(list1)
list1.extend(["a",'b','c'])
print(list1)
print(list1.index(2))
print(list1.pop())#pop() 删除最后一个
print(list1.pop(2))#pop(index) 删除 位置为index 的元素
print(list1)
list1.remove('str')
print("*****")
list2 = [1,2,3,4,5]
print(list2)
list2.reverse()
list2.append(('a','b','c'))
print(list2)
list3 = [22,34,67,2,6,786,33,556,7733,22]
print(list3)
max = max(list3)
print(max)

print(list3)
##print(max(list1))
