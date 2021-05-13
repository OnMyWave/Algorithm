def solution(s):
    zero_cnt = 0
    num = 0
    while s != '1' :
        new_s = ''
        for b in s:
            if b == '1':
                new_s += '1'
            else:
                zero_cnt +=1
        num += 1
        s = bin(int(new_s))
        print(num)
        print(s)
        print()
    answer = [num,zero_cnt]
    return answer

print(solution("110010101001"))