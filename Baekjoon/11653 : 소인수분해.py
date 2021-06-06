N = int(input())
prime_fac = []

while N != 1:
    for i in range(2,N+1):
        if N%i == 0 :
            prime_fac.append(i)
            break
    N //= i 

for fac in prime_fac:
    print(fac)
