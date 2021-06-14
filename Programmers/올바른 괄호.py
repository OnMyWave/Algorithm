def solution(s):
    stack = []
    for bracket in s:
        if len(stack) == 0 :
            stack.append(bracket)
        elif bracket == "(":
            stack.append(bracket)
        else:
            if stack[-1] != "(":
                return False
            else:
                stack.pop()
                
    if len(stack) == 0 :
        return True
    else:
        return False