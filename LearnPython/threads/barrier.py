import threading, time

barrier = threading.Barrier(3)#凑齐指定数量的线程才会执行


def run():
    print(" threadname %s starts "%threading.current_thread().getName())
    barrier.wait()
    print(" threadname %s ends "%threading.current_thread().getName())


if __name__ == "__main__":
    for i in range(1,5):
        threading.Thread(target=run).start()