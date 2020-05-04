for i in range (1,1):
    print("hello{1}{2}{0}".format(i,"aaa",i+1))
for row in range(1,10):
    for col in range(1,row+1):
        print('{} * {} = {}'.format(col,row,row * col),end='\t')
    print()