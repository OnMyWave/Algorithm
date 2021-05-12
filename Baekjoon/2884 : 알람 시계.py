x,y = ( int(i) for i in input().split(' '))
if x == 0:
    if y >= 45:
        print(x,y - 45)
    elif y < 45:
        print(23,60 + (y - 45))
else:
    if y>=45:
        print(x,y-45)
    elif y<45 :
        print(x-1,60+(y-45))