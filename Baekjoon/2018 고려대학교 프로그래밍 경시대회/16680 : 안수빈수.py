import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    while N <=1000000000000000000:
        sum_digit = sum([int(i) for i in str(N)])

        if sum_digit % 2 == 1:
            print(N)
            break
            
        else:
            N += N #다음 배수
 