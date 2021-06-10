# 무지성 침팬지 
def solution(s):
    cnt = True
    
    while cnt :
        cnt = 0
        try:
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
                    cnt += 2
        except:
            pass

    if s == "":
        return 1
    else:
        return 0 

print(solution("abbaaaccddccee"))

# stack 구조 이용
def solution(s):
    stack = []
    
    for c in s:
        if not stack :
            stack.append(c)
        elif c == stack[-1] :
            stack.pop()
        else :
            stack.append(c)
    
    if not stack :
        return 1

    return 0