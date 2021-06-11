def solution(dartResult):
    
    # Bonus Score Table
    table = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    
    # 리스트형으로 변환
    dartResult = [i for i in dartResult]

    # 10이 있으면 1,0이 나눠지기 때문에 묶어주는 처리
    ten_idx = []
    for i in range(len(dartResult)-1):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            ten_idx.append(i)
    
    # 1,0로 나눠진 요소 10으로 바꾸고 삭제
    for i in ten_idx:
        dartResult[i] = "10"
    for i in range(len(ten_idx)):
        del dartResult[ten_idx[i]+1-i]
    
    # 숫자를 기준으로 tokenizing
    idx = [i for i in range(len(dartResult)) if dartResult[i].isdigit()]
    idx.append(len(dartResult))
    print(idx)
    
    # 점수 계산 단계
    answer = 0
    score = 0
    before_trial = 0
    for i in range(3):
        score = 0 
        score += (int(dartResult[idx[i]]))**table[dartResult[idx[i]+1]]
        if idx[i+1] - idx[i] == 3:
            if dartResult[idx[i]+2] == "*":
                answer += before_trial
                score *= 2 
            else:
                score *= -1
        answer += score
        before_trial = score
            
    return answer


print(solution("10S*10S10S*"))

# 인터넷에서 본 솔루션
# 10을 k로 변환한 다음 10으로 다시 처리한 부분이 대단하다 ...
def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)