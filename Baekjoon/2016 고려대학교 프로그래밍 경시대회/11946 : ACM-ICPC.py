n, m, q = map(int,input().split())
scores = [[0 for _ in range(m)] for _ in range(n)]
corrected = [[False for _ in range(m)] for _ in range(n)]
answer = []

for _ in range(q):
    time, t_num, p_num, result = input().split()
    time, t_num, p_num = int(time), int(t_num), int(p_num)

    if result == "AC":
        scores[t_num-1][p_num-1] += time
        corrected[t_num-1][p_num-1] = True
    else:
        if corrected[t_num-1][p_num-1] == False:
            scores[t_num-1][p_num-1] += 20
    
# 출력
# 팀 번호, 푼 문제, 총 시간
for i in range(n):
    cnt = 0
    times = 0
    for k in range(m):
        if corrected[i][k]:
            cnt += 1
            times += scores[i][k]
    answer.append([i+1,cnt,times])

answer.sort(key = lambda x : (-x[1], x[2], x[0]))

for i in answer:
    print(i[0],i[1],i[2])