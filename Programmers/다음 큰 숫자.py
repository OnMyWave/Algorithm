from collections import Counter

def convert(n):
    T = "01"
    div, mod = divmod(n,2)
    if div == 0:
        return T[mod]
    else:
        return convert(div) + T[mod]

def solution(n):
    conv_n = Counter(convert(n))['1']
    for j in range(n+1,1000001):
        if Counter(convert(j))['1'] == conv_n:
            return j
            
    
    