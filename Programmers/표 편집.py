def solution(n, k, cmd):
    answer = ''
    stack = []
    init_n = n
    cnt_c = 0
    for c in cmd:
        c = list(c.split())
        if c[0] == "C":
            cnt = 0
            for i in stack:
                if i <= k+cnt_c :
                    cnt += 1
            if n == k:
                k = n-1
            n -= 1
            stack.append(k+cnt)
            cnt_c += 1
        else:
            cnt_c = 0
            if c[0] == "D":
                k += int(c[1])
            elif c[0] == "U":
                k -= int(c[1])
                
            elif c[0] == "Z":
                stack.pop()
                n += 1

        print(n,k,stack)
    for i in range(init_n):
        if i not in stack:
            answer += "O"
        else:
            answer += "X"

    return answer

print(solution(8,2,["D 2","C","C","C","C","U 2","C","Z","C","D 2","U 2","C"]))