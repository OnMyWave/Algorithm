def solution(s):
    answer = ''
    num_list = [int(i) for i in s.split()]
    answer += str(min(num_list)) + " " +str(max(num_list))
    
    return answer