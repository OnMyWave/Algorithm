def solution(s, n):
    # ASC II
    # 영어 대문자 65 ~ 90
    # 영어 소문자 97 ~ 122
    # 공백       32
    answer = ''
    for string in s:
        if string == " ":
            answer += string
        elif ord(string) <= 90 :
            if ord(string) + n > 90 :
                answer += chr(ord(string)+n-26)
            else:
                answer += chr(ord(string) + n)
        else:
            if ord(string) + n > 122:
                answer += chr(ord(string)+n-26)
            else:
                answer += chr(ord(string) + n)

    return answer