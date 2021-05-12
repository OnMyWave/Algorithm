score=[]
for _ in range(5):
    score.append(int(input()))
for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40
average = sum(score)//5
print(average)