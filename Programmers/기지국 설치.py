def solution(n, stations, w):
    maps = [0] * n 
    for station in stations : 
        station -= 1
        for i in range(-w,w+1):
            if (station + i >= n or station + i < 0):
                continue
            else:
                maps[station + i] = 1
    answer = 0 
    cnt = 0       
    for j in range(n):
        if maps[j] == 0 : 
            cnt += 1
        if cnt == (w + 1) :
            answer += 1
            for i in range(-w,w+1):
                if (station + i >= n or station + i < 0):
                    continue
                else:
                    maps[station + i] = 1
            cnt = 0 

    return answer