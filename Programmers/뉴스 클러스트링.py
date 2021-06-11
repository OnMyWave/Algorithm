import re

def solution(str1, str2):
    
    # 집합 선언
    intersection_set = 0 
    set1 = []
    set2 = []
    
    # 대문자 소문자 차이 무시
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 영문자로 된 글자 쌍만 유효화
    for i in range(len(str1)-1):
        if not re.search('[^a-z]',str1[i:i+2]) :
            set1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if not re.search('[^a-z]',str2[i:i+2]) :
            set2.append(str2[i:i+2])
    length1 = len(set1)
    length2 = len(set2)

    # set
    if len(set1) == len(set2) == 0:
        return 65536
    
    elif len(set1) <= len(set2):
        for i in range(len(set1)):
            a = set1.pop()
            if a in set2 : 
                set2.remove(a)
                intersection_set += 1
    else:
        for i in range(len(set2)):
            a = set2.pop()
            if a in set1:
                set1.remove(a)
                intersection_set += 1
                
    return int(intersection_set / (length1 +length2 - intersection_set) * 65536)
                
        