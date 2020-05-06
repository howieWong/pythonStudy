'''
_thread模块 比较底层
threading 封装了_thread
'''
# 启动一个线程
import threading

# unsafe
num = 0

lock = threading.Lock()


def run():
    # print("sub thread **%s** starts" % threading.current_thread().getName())
    global num
    for i in range(0, 1000000):
        with lock:
            num += 1
        '''    lock.acquire()
            try:
                num += 1
            finally:
                lock.release()'''
        # print(num,"sub")


if __name__ == "__main__":
    # print("main thread --%s-- starts" % (threading.current_thread().getName()))
    # run()
    # t = threading.Thread(target=run,name="sub thread")
    # t = threading.Thread(target=run)
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
