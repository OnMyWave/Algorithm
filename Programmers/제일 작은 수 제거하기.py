def solution(arr):
    answer = []
    
    if len(arr) == 1:
        return [-1]
    
    else:
        sorted_arr = sorted(arr)
        minOfArr = sorted_arr[0]
        idx = -1
        for i in range(len(arr)):
            if minOfArr == arr[i]:
                idx = i
        return arr[:idx] + arr[idx+1:]
            
    