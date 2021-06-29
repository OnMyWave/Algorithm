import sys

T = int(sys.stdin.readline())
wire = []

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    wire.append([a,b])

wire.sort(key = lambda x : x[0])
print(wire)

num_list = []
if len(wire) <= 1 :
    print(0)
else:
    answer = []
    for i in range(1,len(wire)):
        cnt = 0
        for j in range(i):
            if wire[i][1] < wire[j][1]:
                cnt += 1
        answer.append(cnt)
    print(answer)

