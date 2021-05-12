dan=input()
alpha=[]
for i in range(97,123):
    alpha.append(chr(i))
for i in alpha:
    print(dan.find(i),end=' ')