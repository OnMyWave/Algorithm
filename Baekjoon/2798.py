N,M = map(int,input().split())
card_list = list(map(int,input().split()))
length = len(card_list)
result = 0
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            if card_list[i]+card_list[j]+card_list[k] > M :
                continue
            else:
                result = max(result,card_list[i]+card_list[j]+card_list[k])

print(result)
