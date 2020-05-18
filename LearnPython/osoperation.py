import  os

print(os.path.realpath(r"C:\Users\lenovo\Desktop\file.txt"))
print(os.name)# windows
#print(os.environ)#获取操作系统中的环境变量
print(os.curdir)
print(os.path.realpath(os.curdir))
print(os.getcwd())
print(os.listdir(r"C:\Users\lenovo\Desktop"))
#print(os.stat(r"C:\Users\lenovo\Desktop\file.txt"))
#os.rename(r"C:\Users\lenovo\Desktop\file.txt",r"C:\Users\lenovo\Desktop\tmp.txt")
#print(os.path.abspath(".\osoperation.py"))
dir = "C:\\Users\\lenovo\\Desktop\\"
file = "tmp.txt"
print(os.path.join(dir, file))
print(os.path.split(r"C:\Users\lenovo\Desktop\file.txt"))#('C:\\Users\\lenovo\\Desktop', 'file.txt')
print(os.path.splitext(r"C:\Users\lenovo\Desktop\file.txt"))#('C:\\Users\\lenovo\\Desktop\\file', '.txt')
list1 = os.listdir(r"C:\Users\lenovo\Desktop\新建文件夹")
for f in list1:
    if os.path.isdir(f):
        print(os.listdir(f))
    print(f)



