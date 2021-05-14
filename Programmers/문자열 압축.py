def solution(s):
    answer = 0
    length = len(s)//2
    str_list = []
    if len(s) == 1:
        return 1
    
    for i in range(1,length+1):
        a = len(s)//i
        str_component = ""
        j = 0
        count = 1
        while j != a+1:
            if s[i*j:i*(j+1)] == s[i*(j+1):i*(j+2)]:
                count += 1
            else:
                if count == 1:
                    str_component += s[i*j:i*(j+1)]
                else:
                    str_component += str(count)+s[i*j:i*(j+1)]
                    count = 1
            j+=1
        str_list.append(str_component)
    str_list = list(map(len,str_list))
    return min(str_list)