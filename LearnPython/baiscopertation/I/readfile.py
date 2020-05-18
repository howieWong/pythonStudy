# read file

''' '''

'''
open file
    open(path,flag[,encoding][,errors])
    r  readonly
    rb readonly with binary
    r+ readwrite
    w  write,if file exist,override it else,create a new file
    wb
    w+ readwrite
    a  append
    a+
read
close
'''
file = r"C:\Users\lenovo\Desktop\速盘极速版激活码.txt"
def readfile(file):
    try:
        file = open(file, "r")
        print(file.readlines())
        # 修改文件描述符的位置，即重头开始读
        file.seek(0)
        str = file.readline()
        while str:
            print(str)
            str = file.readline()
        # print(file.read())
    except (FileExistsError, FileNotFoundError) as e:
        print(e)
    finally:
        if file:
            file.close()


def readfile2(file):
    with open(file,"r")  as f2:
        str = f2.readline()
        while str:
            print(str)
            str = f2.readline()

#readfile2(file)
