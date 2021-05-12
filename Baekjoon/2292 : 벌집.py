N = int(input())

# 6,12,18,24,...: 1, 7 , 19 , 37
#AN+1 = AN + 6N (N=1,2,3,..)
#AN=1+3n(n-1) (N=1,2,3,...)

def A(n): #  Ak<=n<=Ak+1 : return k
    return 1 + 3 * n * (n - 1)
floor = 0
if N== 1:
    print(1)
else:
    while A(floor) < N :
        floor += 1
    print(floor)

