def isPrime(number):
    if number <= 1 :
        return False
    for i in range(2,number):
        if number % i == 0 :
            return False
    return True

M, N = map(int,input().split())
prime_number = []

for i in range(M,N+1):
    if isPrime(i):
        prime_number.append(i)

for prime in prime_number:
    print(prime)



