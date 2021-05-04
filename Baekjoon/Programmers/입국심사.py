def solution(n,times):
    time = 0
    length = len(times)
    current_list = [True] * length
    f_num = 0
    while f_num < n:
        time += 1
        for i in times:
            if time % i == 0 :
                f_num += 1

    return time

print(solution(6,[7,10]))