T = int(input())

zero_cnt = [1,0]
one_cnt = [0,1]

for _ in range(T):
    N = int(input())
    fib_list = [[1,0],[0,1]]
    for i in range(2,N+1):
        fib_list.append([fib_list[i-1][0]+fib_list[i-2][0],fib_list[i-1][1]+fib_list[i-2][1]])
    
    print(' '.join(list(map(str,fib_list[N]))))