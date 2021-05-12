C = int(input())
for _ in range(C):
    N,*student = map(int,input().split())
    average = sum(student)/N
    overAverage = 0
    for i in student:
        if i > average:
            overAverage+=1
    print("%.3f%%"%(overAverage/N*100))

