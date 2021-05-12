A,B,C=map(int,input().split(' '))
number = 0
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)