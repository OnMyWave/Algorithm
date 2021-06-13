def makeOne(n,cnt):
    if n == 1:
        return cnt
    else:
        cnt += 1
        if n % 3 == 0 :
            return makeOne(n//3,cnt)
        elif (n - 1) % 3 == 0 :
            return makeOne(n-1,cnt)
        elif n % 2 == 0 :
            return makeOne(n//2,cnt)
        else :
            return makeOne(n-1,cnt)

print(makeOne(10,0))
print(makeOne(3,0))
print(makeOne(1000,0))