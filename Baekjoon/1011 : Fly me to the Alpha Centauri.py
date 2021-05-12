def func(x):
    k=0
    while x> (k+1)**2:
        k+=1
    return k

T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    d = y-x
    N = func(d)
    if (N+1)**2 - N <= d:
        print(2*N+1)
    else:
        print(2*N)