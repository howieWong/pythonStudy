import threading

num = 0
local = threading.local()


def run(x):
    x += 1


def fun():
    local.x = num
    for i in range(1, 100000):
        run(local.x)
    print("%s - %d" % (threading.current_thread().name, local.x))


if __name__ == "__main__":
    th1 = threading.Thread(target=fun,name="th1")
    th2 = threading.Thread(target=fun, name="th2")
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(num)