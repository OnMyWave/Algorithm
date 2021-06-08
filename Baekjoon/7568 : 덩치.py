N = int(input())
people = []

for _ in range(N):
    x,y = map(int,input().split())
    people.append((x,y))

for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
    print(cnt,end = " ")

