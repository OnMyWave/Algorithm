def solution(msg):
    answer = []
    dic = [chr(i+65) for i in range(26)]
    while msg :
        i = 1
        print(msg)
        while True:
            if i >= len(msg):
                answer.append(dic.index(msg[:i])+1)
                msg = ""
                break
            elif msg[:i+1] in dic:
                i += 1
            else:
                answer.append(dic.index(msg[:i])+1)
                dic.append(msg[:i+1])
                msg = msg[i:]
                i = 1
                break
        print(dic)
        print(answer)
    return answer

# print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))