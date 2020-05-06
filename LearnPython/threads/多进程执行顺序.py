import os
import time
from multiprocessing import Process
num = 100
def subPro(*args,**kwargs):
    print("sub process begins",args,kwargs)
    print(type(args))
    print(type(kwargs))
    time.sleep(0.1)
    print("sub process ends")
'''
*args 将参数打包成tuple
**kwargs 打包关键字参数 dic
'''

if __name__ == "__main__":
    print(os.cpu_count(),"fff")
    print("main process begins")
    subPro(x=1,y=2,z=3)
    sub = Process(target=subPro,args=("a","b","c",[1,2,3],{"name":"jack","age":15}))
    sub.start()
    sub.join()

    print("num=%d"%3)
    print("main process ends")
