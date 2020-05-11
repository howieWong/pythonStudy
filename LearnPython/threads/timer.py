import threading

def run():
    print("ding shi ")
threading.Timer(3,run).start()