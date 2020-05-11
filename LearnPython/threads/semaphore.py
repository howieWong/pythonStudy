import threading,time

semaphore = threading.Semaphore(5)#控制线程执行的数量
def run():
    with semaphore:
        for i in range(1,4):
            print("name=%s excute: i=%d "%(threading.current_thread().name,i))
            time.sleep(0.1)

if __name__ == "__main__":
    for i in range (1,8):
        th = threading.Thread(target=run,name=i)
        th.start()