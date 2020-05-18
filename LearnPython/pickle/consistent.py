import pickle

list = [1, 2, 3, 4, 'a', 'b', 'c', "hello world"]
file = open(r"C:\Users\lenovo\Desktop\file.txt", "wb")
pickle.dump(list, file)
file.close()

file2 = open(r"C:\Users\lenovo\Desktop\file.txt", "rb")
# print(file.readline())
list = pickle.load(file2)
print(list)
file.close()
'''
list tuple set dict 持久化
pickle.dump(obj,file)
obj = pickle.load(file)
'''