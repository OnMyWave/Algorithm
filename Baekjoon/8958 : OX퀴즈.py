T = int(input())
for _ in range(T):
    OX = input()
    score = 0
    combo = 0
    for i in OX:
        if i == 'O':
            combo += 1
        else:
            combo = 0
        score+=combo
    print(score)


