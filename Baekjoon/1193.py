'''def sum_1toN(n):
    return n*(n+1)/2

def find_n(X):
    if X==1:
        return 1
    else:
        n=1
        while X//(sum_1toN(n)) == 0:
            n+=1
        return n
'''
X=int(input())
answer = []
while len(answer) == X:
    a=1; b=1;
    answer.append(f'{a}/{b}')
    while b!=1:
        a-=1
        b+=1
    while a!=1:
        b-=1
        a+=1

print(answer[X-1])
