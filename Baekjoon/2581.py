import math

M = int(input())
N = int(input())

primeList = []

for a in range(M,N):
    num = 0
    i = int(math.sqrt(a))
    for j in range(2,i):
        if i % j == 0:
            num += 1
    if num == 0 :
        primeList.append(i)

if not primeList:
    print(-1)
else:
    print(sum(primeList))
    print(primeList[0])






