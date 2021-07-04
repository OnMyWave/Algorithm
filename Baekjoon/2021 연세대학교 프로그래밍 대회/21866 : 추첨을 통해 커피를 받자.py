scores = list(map(int,input().split()))
max_score = [100,100,200,200,300,300,400,400,500]

hacker = False
for i in range(9):
    if scores[i] > max_score[i]:
        hacker = True

if hacker :
    print("hacker")
else:
    if sum(scores) >= 100:
        print("draw")
    else:
        print("none")
