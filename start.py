def sideTriPtrn(rows):
    x=round(rows/2)
    for i in range(rows):
        if i <=round(rows/2):
            print('* ' * i)
        if i >=round(rows/2):
            x=round(x-1)
            print('* ' * x)

sideTriPtrn(50)