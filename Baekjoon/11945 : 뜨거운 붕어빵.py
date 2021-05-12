N,M = map(int,input().split())
mold = []
for i in range(N):
    row = list(input())
    mold.append(row)
for j in range(N):
    mold[j]= mold[j][::-1]

for k in mold:
    output=""
    for l in k:
        output+=l
    print(output)