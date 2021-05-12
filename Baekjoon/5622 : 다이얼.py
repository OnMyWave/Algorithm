word = [i for i in input()]
num = [['A','B','C'],['D','E','F'],['G','H','I']
    ,['J','K','L'],['M','N','O'],['P','Q','R','S']
    ,['T','U','V'],['W','X','Y','Z']]
count = 0

for i in word:
    for j in range(len(num)):
        if i in num[j]:
            count += (j+3)

print(count)