# Solution 1: 무지성 침팬지 
# 각 종류별 stack으로 받았기 떄문에 '({)}'와 같은 케이스에서 오류 발생

def isCorrectBracket(s):
    opening_brackets = ['(','[','{']
    closing_brackets = [')',']','}']
    brackets = [[] for _ in range(3)]
    
    # bracket 단위 순회
    for bracket in s:
        if bracket in opening_brackets:
            brackets[(opening_brackets.index(bracket))].append(bracket)
        else:
            if len(brackets[(closing_brackets.index(bracket))]) == 0 :
                return False
            else : 
                if brackets[(closing_brackets.index(bracket))][-1] == opening_brackets[closing_brackets.index(bracket)]:
                    brackets[(closing_brackets.index(bracket))].pop()
        
    cnt = 0
    for i in range(3):
        cnt += len(brackets[i])
    
    if cnt :
        return False
    else:
        return True
            
# 무지성 침팬지가 아니라 사람다운 생각 : dictionary 이용

def isCorrectBrackets(s):
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }            
    for bracket in s:
        if bracket not in table :
            stack.append(bracket)
        elif not stack or table[bracket] != stack.pop():
                return False
    if len(stack) == 0:
        return True

        
def solution(s):
    answer = 0 
    for i in range(len(s)):
        changed_s  = s[i:] + s[:i]
        if isCorrectBrackets(changed_s):
            answer += 1
    return answer