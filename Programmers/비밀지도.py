def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    arr1 = [str(bin(i)) for i in arr1]
    arr2 = [str(bin(i)) for i in arr2]
    for i in range(n):
        arr1[i] = arr1[i][2:]
        arr2[i] = arr2[i][2:]
        
    for i in range(n):
        if len(arr1[i]) != n:
            while len(arr1[i])<n:
                arr1[i] = "0" + arr1[i]
                
        if len(arr2[i]) != n:
            while len(arr2[i])<n:
                arr2[i] = "0" + arr2[i]
    
    for i in range(n):
        for j in range(n):
            if int(arr1[i][j])+int(arr2[i][j]) >= 1:
                answer[i] += "#"
            else:
                answer[i] += " "
    
        
    

    return answer