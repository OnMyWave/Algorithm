def solution(s):
    word_list = s.split(" ")
    answer = ""
    for word in word_list:
        part = ""
        length = len(word)
        for j in range(length):
            if j % 2 == 0 : 
                part += word[j].upper()
            else:
                part += word[j].lower()
        answer += part + " "
    return answer[:-1]