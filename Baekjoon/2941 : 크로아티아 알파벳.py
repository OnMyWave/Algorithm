cro = input()

alphabet = ['c=','c-','dz=','d-','lj',
            'nj','s=','z=']
count = 0

for i in alphabet:
    while i in cro:
        cro = cro.replace(i,'0',1)
        count += 1

for j in cro:
    if j != '0':
        count += 1

print(count)

