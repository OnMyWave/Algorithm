def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x: (x[1] - x[0], x[0]))
    for dungeon in dungeons : 
        if k >= dungeon[0] : 
            answer += 1
            k -= dungeon[1]

    return answer