dic1= {"key1":"value","key2":2,"key3":[1,2,3]}
print(dic1["key1"])#没有报错 KeyError
print(dic1.get("k"))#没有返回None
dic1["key3"]="3"
print(dic1)
dic1["key4"]="value4"
print(dic1)
##删除
dic1.pop("key4")
print(dic1)

###遍历
for k in dic1.values():
    print(k,end=" ")
print()
for k , v in dic1.items():
    print("key=",k,"value=",v,end=" ")
print()
for index,key in enumerate(dic1):##enumerate() 获得index 和 key，对list来水 是序号和值
    print("index=%d,key=%s"%(index,key))

str="today is a good day! tomorrow is good day"
count={}
for str in str.split():
    if count.get(str):
        count[str] +=1
    else:
        count[str] = 1
print(count)