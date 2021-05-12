N = input().upper()
a = list(N)
b = list(set(a))
count = 0
c = []
for i in b:
    c.append(a.count(i))
c.sort()
if len(N) == 1:
    print(N)
else:
    if c[-1] == c[-2]:
        print('?')
    else:
        for i in b:
            if a.count(i) == c[-1]:
                print(i)


