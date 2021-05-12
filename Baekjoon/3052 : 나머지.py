numberList = []
remainder = []
for i in range(10):
    numberList.append(int(input()))
for j in numberList:
    remainder.append(j%42)
remainder.sort()
count = 1
check = remainder[0]
for k in remainder:
    if k != check:
        count+=1
        check = k
print(count)