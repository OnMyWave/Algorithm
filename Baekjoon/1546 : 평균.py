N = int(input())
score = [int(i) for i in input().split(' ')]
maxScore = max(score)
average = 0
for i in range(len(score)) :
    score[i] = score[i]/maxScore*100
    average += score[i]
print(average/N)



