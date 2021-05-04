N = int(input())

result = []

def maker(n):
    n_component = [ i for i in str(n)]
    new_n = n
    for i in n_component:
        new_n += int(i)
    return new_n

for i in range(1,N+1):
    if maker(i) == N:
        result.append(i)

if len(result) == 0 :
    print(0)
else:
    print(min(result))
