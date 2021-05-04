
#A
print("고려대학교")

#B

A,B = map(int,input().split())
C,D = map(int,input().split())

if abs(A+D) >= abs(B+C):
    print(B+C)
else:
    print(A+D)

#C

N,M = map(int,input().split())
print((str(N)*N)[:M])

#D

N,M = map(int,input().split())
mold = []
for i in range(N):
    row = list(input())
    mold.append(row)
for j in range(N):
    mold[j]= mold[j][::-1]

for k in mold:
    output=""
    for l in k:
        output+=l
    print(output)



#E
N,M,Q = map(int,input().split())

# N : 대회에 참가한 팀 수  M : 문제 수
#input : 경과 시간 / 팀 번호 / 문제 번호 / 채점 결과
#채점 결과 : AC/ RE / TLE / WA
#output : 팀 번호 / 푼 문제 수 / 총 시간
result = [[i,0,0] for i in range(N)]
submit_log = []
for i in range(Q): # 채점 log Q
    current_log = list(input().split())
    submit_log.append(current_log)
    current_log[0:3] = map(int,current_log[0:3])  #리스트의 일부만 map을 이용해서 자료형 변환
    if current_log[3] == "AC":
        result[current_log[1]][1] += 1
        result[current_log[1]][2] += current_log[0]
        for i in submit_log:
            if i[1] == current_log[1] and i[2] == current_log[2] :
                result[current_log[1]][2] += 20

grade = sorted(result[1:], key = lambda x: (-x[1], x[2], x[0]))
# 리스트 정렬 부분
# 튜플 형태로 아래 조건 서술
# 첫 번째로 2번째 component에 대해 부호음수 -> 내림차순
# 두 번째로 3번째 component에 대해 부호양수 -> 오름차순
# 세 번째로 1번째 component에 대해 부호양수 -> 오름차순
for i in grade:
    print(i[0], i[1], i[2])


#F 이런 반전이


