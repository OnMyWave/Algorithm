N = int(input())

primeNumber = 0

inputNumber = map(int,input().split(' '))

for i in inputNumber :
    num = 0
    if i == 1:
        continue

    for j in range(2,i):
        if i%j == 0:
            num += 1

    if num == 0 :
        primeNumber += 1

print(primeNumber)
