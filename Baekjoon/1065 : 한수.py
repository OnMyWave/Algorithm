N = input()

count = 0

for i in range(1,int(N)+1):
    if i//100 == 0:
        count+=1
    else:
        k=str(i)
        if int(k[1])*2 == int(k[0])+int(k[2]):
            count+=1
print(count)