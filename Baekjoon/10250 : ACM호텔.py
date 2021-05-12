T = int(input())
for _ in range(T):
    H, W, N=map(int, input().split())
    A = N % H if N % H != 0 else H
    B = N // H + 1 if N % H != 0 else N //H
    if B>= 10 :
        print(f'{A}{B}')
    else:
        print(f'{A}0{B}')

