N = int(input())

def fac(N):
    if N == 1:
        return 1
    elif N == 0:
        return 1
    else:
        return N*fac(N-1)

print(fac(N))