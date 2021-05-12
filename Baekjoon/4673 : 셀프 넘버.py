def D(N):
    a = str(N)
    b = 0
    for i in a:
        b+=int(i)
    return N + b
man = [ i for i in range(1,10001)]
selfNumber = []
for i in range(1,10001):
    selfNumber.append(D(i))
for i in selfNumber:
    if i in man:
        man.remove(i)
for i in man:
    print(i)

