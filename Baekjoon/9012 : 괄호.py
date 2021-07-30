import sys

T = int(sys.stdin.readline())

def isVPS(bracket):
    stack = []

    for b in bracket:
        if b == "(":
            stack.append(b)
        else:
            try:
                stack.pop()
            except:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"    

for _ in range(T):
    bracket = sys.stdin.readline()
    print(isVPS(bracket))