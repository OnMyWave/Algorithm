N = int(input())
people = []

for _ in range(N):
    weight, height = map(int,input().split())
    people.append([weight,height])



print(people)