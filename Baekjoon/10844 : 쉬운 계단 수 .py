from collections import deque

N = int(input())
num_list = deque([str(i) for i in range(1,10)])
length = 9

for j in range(1,N):
    cnt = 0 
    for i in range(length):
        p = num_list.popleft()
        if p[-1] == "0" :
            num_list.append(p + "1")
            cnt += 1
        elif p[-1] == "9":
            num_list.append(p + "8")
            cnt += 1
        else:
            num_list.append(p+ str(int(p[-1])-1))
            num_list.append(p+ str(int(p[-1])+1))
            cnt += 2
    length = cnt

print(length%1000000000)
