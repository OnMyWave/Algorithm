def solution(number, k):
    answer = ''
    cnt = 0 
    idx_list = []
    while cnt < k:
        for i in range(len(number)-1):
            if number[i] < number[i+1]:
                if i == 0 :
                    number = number[1:]
                else:
                    number = number[:i] + number[i+1:]
                break
        cnt += 1
    return number