def isPrime(number):
    if number <= 1 :
        return False
    for i in range(2,number):
        if number % i == 0 :
            return False
    return True

M = int(input())
N = int(input())
prime_number = []

for i in range(M,N+1):
    if isPrime(i):
        prime_number.append(i)
if len(prime_number):
    print(sum(prime_number))
    print(min(prime_number))
else:
    print(-1)



