# 数和字符串
# 列表 []
students = ["a", "b", "c", "d", "e"]
print("{}+{}".format(students[0],students[1]))
students[0]= "aa"
print("{}+{}".format(students[0],students[1]))

print(students[0],"==",students[1])
print(students[0]+"---"+students[1])

# 元组
students2 = ("1","2","3")
print(students2)
#students2[1]="3"

#集合 set\
print("set")
a=set("abcdefffff")
print(a)
b=set("cdfmz")
print (a&b)
print(a|b)
print(a - b)
new = set(a)
print(new)

print(set(set("hhjj")))
#dictionary
info={"name":"tmg","age":10}
print(info["name"])
info["hobby"]="games"
print(info["hobby"])
info["age"]=20
print(info)

print("abc\n"*5)