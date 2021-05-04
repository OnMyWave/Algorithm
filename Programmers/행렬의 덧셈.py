def solution(arr1, arr2):
    row = len(arr1)
    column = len(arr1[0])
    answer = [[arr1[i][j] + arr2[i][j] for j in range(column) ] for i in range(row)]

    return answer