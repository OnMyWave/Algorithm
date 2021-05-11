from collections import deque

def solution(priorities, location):
    d = deque(priorities)
    print_cnt = 0
    loc_list = deque(i for i in range(len(priorities)))
    while d:
        if d[0] == max(d):
            print_cnt += 1
            if loc_list[0] == location:
                return print_cnt
            d.popleft()
            loc_list.popleft()
            
        else:
            not_max = d.popleft()
            d.append(not_max)
            cnt = loc_list.popleft()
            loc_list.append(cnt)