def convert(n):
    T = "124"
    div, mod = divmod(n-1,3)
    if div == 0:
        return T[mod]
    else:
        return convert(div) + T[mod]

def solution(n):
    answer = convert(n)
  
        
    return answer