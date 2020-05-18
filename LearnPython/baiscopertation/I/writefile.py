path = r"C:\Users\lenovo\Desktop\testwrite.txt"
'''
file = open(path,"a")
file.write("hello world   aaa\n\r")
file.flush()#刷新缓冲区，立即写入文件
file.close()
'''

with open(path,"a") as filedescription:
    filedescription.write("hello")