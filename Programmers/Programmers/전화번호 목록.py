import re

def solution(phone_book):
    number_list = [[] for _ in range(10)]
    for number in phone_book:  # Hash 형식으로 phone_number_book 만들기
        number_list[int(number[0])].append(number)
    
    number_list = sorted(number_list, key = lambda x : len(x))
    for i in range(10):
        number_list[i].sort()
    for idx in range(10): # 0 ~ 9 각 숫자마다 탐색
        length = len(number_list[idx])
        for i in range(length): # 완전 탐색
            prefix = number_list[idx][i]
            p = re.compile('^'+prefix)
            for j in range(i+1,length):
                if p.match(number_list[idx][j]):
                    return False
            
        
    
    return True