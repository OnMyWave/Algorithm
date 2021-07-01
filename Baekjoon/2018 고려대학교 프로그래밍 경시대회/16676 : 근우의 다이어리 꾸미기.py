N = int(input())
i = 0
if N <= 10:
    print(1)
else:
    while True:
        i += 1
        if int("1"*(i+1))> N >= int("1"*i):
            break

    print(i)
