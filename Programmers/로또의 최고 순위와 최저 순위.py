def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_list = [6,6,5,4,3,2,1]
    zero_cnt = 0
    for number in lottos:
        if number in win_nums:
            cnt += 1
        elif number == 0 :
            zero_cnt += 1
    if cnt + zero_cnt >= 7 :
        answer.append(cnt_list[cnt])
        answer.append(cnt_list[6])
    else:
        answer.append(cnt_list[cnt])
        answer.append(cnt_list[cnt+zero_cnt])
    answer.sort()
    return answer