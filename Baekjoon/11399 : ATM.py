N = int(input())
people = sorted(list(map(int,input().split())))

time = 0 
sum_time = 0

for i in people:
    time += i
    sum_time += time

print(sum_time)