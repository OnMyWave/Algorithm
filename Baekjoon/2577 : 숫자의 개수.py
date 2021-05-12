a = int(input())
b = int(input())
c = int(input())
mul = a*b*c
for i in range(10):
    count = 0
    for j in str(mul):
        if int(j) == i :
            count+=1
    print(count)