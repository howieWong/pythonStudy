import os
import time
from multiprocessing import Process

'''
os.getpid() 子进程
os.getppid() 父进程
'''
def run(str):
    while True:
        print("hello world %s pid=%s ppid=%s"%(str,os.getpid(),os.getppid()))
        time.sleep(1)


if __name__ == "__main__":
    p = Process(target=run,args=("sub process",))
    p.start()
    while True:
        print("main process mpid= %s"%(os.getpid()))
        time.sleep(1)