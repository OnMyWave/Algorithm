def solution(places):
    mold = [[[-1,0],[1,0],[0,1],[0,-1]],[[-2,0],[2,0],[0,2],[0,-2]],[[-1,-1],[-1,1],[1,1],[1,-1]]]
    answer = []

    def social_distancing(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P": 
                    for m in mold[0] : # 사람끼리 거리가 1일 때
                        if i + m[0] < 0 or i + m[0] > 4 or j +m[1] < 0 or j + m[1] > 4:
                            continue
                        else:
                            if place[i+m[0]][j+m[1]] == "P":
                                return 0

                    for m in mold[1]: # 사람끼리 거리가 2일 때 -> 무조건 사이에 X 필요
                        if i + m[0] < 0 or i + m[0] > 4 or j +m[1] < 0 or j + m[1] > 4:
                            continue
                        else:
                            if place[i+m[0]][j+m[1]] == "P":
                                if place[i+int(m[0]/2)][j+int(m[1]/2)] != "X":
                                    return 0

                    for m in mold[2]: # 대각선인 경우, 사이에 X 두 개 필요
                        if i + m[0] < 0 or i + m[0] > 4 or j +m[1] < 0 or j + m[1] > 4:
                            continue
                        else:
                            if place[i+m[0]][j+m[1]] == "P":
                                if place[i+m[0]][j] == "X" and place[i][j+m[1]] == "X":
                                    continue
                                else:
                                    return 0
        return 1

    for place in places:
        answer.append(social_distancing(place))
                        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))