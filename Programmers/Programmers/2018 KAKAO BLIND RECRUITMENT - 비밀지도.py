def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    newArr1 =[]
    newArr2 = []
    map1 = []
    map2 = []
    for component in arr1:
        newArr1.append(bin(component))
    for component in arr2:
        newArr2.append(bin(component))

    for component in newArr1:
        a = []
        for i in range(2,len(component)):
            a.append(component[i])
        if len(a) == n-1:
            a.insert(0,0)
        map1.append(a)

    for component in newArr2:
        a = []
        for i in range(2,len(component) ):
            a.append(component[i])
        if len(a) == n-1:
            a.insert(0,0)
        map2.append(a)

    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                answer[i] += "#"
            else:
                answer[i] += " "

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))