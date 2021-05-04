def solution(s):
    answer = 0
    str_list = {}
    for string in s:
        str_list[string] = 0
    for string in s:
        str_list[string] +=1
    for key,value in str_list.items():
        if value % 2 == 1:
            answer+=1
    return answer

print(solution("aabbbccd"))
print(solution("abebeaedeac"))
print(solution("aabb"))