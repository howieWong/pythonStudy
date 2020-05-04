'''age=input()
print("age="+age)

year=input("please input year")
month=input("please input month")
print("year={},month={}".format(year,month))
'''
for row in range(1,10):
    for col in range(1,row + 1):
        print(row , "*" , col , "=" ,row*col,end="\t")
    print()


