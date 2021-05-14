def is_balanced(s):
    if s.count('(') == s.count(')'):
        return True
    else:
        return False

def is_correct(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                return False
    if not stack:
        return True

def swap_braket(s):
    result = ''
    for i in s:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result
    
def solution(p):
    result = ''
    if p == '':
        return p
    for i in range(1, len(p)+1):
        u = p[:i]
        v = p[i:]
        if is_balanced(u) and is_balanced(v):
            break
    print(u, v)
    if is_correct(u):
        result = u + solution(v)
    else:
        result = '(' + solution(v) + ')'
        temp = swap_braket(u[1:-1])
        result += temp
    return result