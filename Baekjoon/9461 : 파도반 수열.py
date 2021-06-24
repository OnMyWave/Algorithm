T = int(input())


for _ in range(T):
    dp = [1,1,1,2,2]
    N = int(input())
    if N <= 5:
        print(dp[N-1])
    else:
        for i in range(5,N):
            dp.append(dp[i-5]+dp[i-1])
        print(dp[N-1])