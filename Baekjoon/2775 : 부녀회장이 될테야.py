T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1,n+1)]
    for i in range(k):
        for j in range(n-1):
            arr[j+1]+=arr[j]
    print(arr[-1])        