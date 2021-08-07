N, Q = map(int,input().split())
fan_list = []
for idx in range(1,N+1):
    P, K, C = map(int,input().split())
    cost = P 
    time = N
    i = 1
    while time > 0:
        cost += i * C
        i += 1
        time -= K
    fan_list.append([idx,cost]) 

print(sorted(fan_list, key = lambda x: (x[1],x[0])))
