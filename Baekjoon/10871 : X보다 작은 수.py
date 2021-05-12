N,X = map(int,input().split())
list1 = [int(i) for i in input().split()]
list2 = []
for i in list1:
    if i<X:
        list2.append(i)
for i in list2:
    print(i,end=' ')