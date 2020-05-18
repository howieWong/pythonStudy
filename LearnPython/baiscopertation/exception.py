def divide(a, b):
    print(a // b)


#divide(4, 0)


def divide2(a, b):
    try:
        print(a // b)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("over")

divide2(3,0)