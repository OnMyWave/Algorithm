from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer = []
    
    for i in course:
        menu_comb = []
        for order in orders:
            menu_comb += map(''.join,(list(map(sorted,combinations(order,i)))))
        print(menu_comb)
        menu_comb = [i for i in Counter(menu_comb).most_common() if i[1]>=2]
        try:
            max_length = menu_comb[0][1]
            for i in menu_comb:
                if i[1] == max_length :
                    answer.append(i[0])
                else:
                    break
        except:
            pass
    
    answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))