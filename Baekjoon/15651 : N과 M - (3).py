from itertools import product

N, M = map(int,input().split())
ints = [i for i in range(1,N+1)]
num_list = [i for i in product(ints,repeat = M)]


for i in num_list:
    print(' '.join(list(map(str,i))))