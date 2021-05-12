A,B = map(int,input().split())
C,D = map(int,input().split())

if abs(A+D) >= abs(B+C):
    print(B+C)
else:
    print(A+D)


