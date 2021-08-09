def solution(scores):
    answer = ''
    length = len(scores)
    score = [[s[i] for s in scores] for i in range(length)]
    for i in range(length):
        average = 0
        cnt = 0 
        if (score[i].index(max(score[i])) == i and score[i].count(max(score[i])) == 1) or (score[i].index(min(score[i])) == i and score[i].count(min(score[i])) == 1 ) :
            for j in range(length):
                if j == i :
                    continue
                else:
                    cnt += 1
                    average += score[i][j]
        else:
            for j in range(length):
                cnt += 1
                average += score[i][j]
        if average/cnt >= 90 :
            answer += "A"
        elif average/cnt >= 80 :
            answer += "B"
        elif average/cnt >= 70 :
            answer += "C"
        elif average/cnt >= 50 :
            answer += "D"
        else:
            answer += "F"
    return answer