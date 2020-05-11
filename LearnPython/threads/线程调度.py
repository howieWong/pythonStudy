import threading,time

cond = threading.Condition()


def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(0.2)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            time.sleep(0.2)
            cond.notify()
            cond.wait()

if __name__ == "__main__":
    th1 = threading.Thread(target=run1,name="th1")
    th2 = threading.Thread(target=run2,name="th2")
    th1.start()
    th2.start()
