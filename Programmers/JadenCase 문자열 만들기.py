def solution(s):
    answer = ''
    s = s.lower()
    word_list = [word for word in s.split()]
    for word in word_list:
        word = word.capitalize()
        answer += word + " "
    return answer[:-1]