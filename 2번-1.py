def recur_func(arr, num):
    answer = num
    if len(arr) == 1:
        return answer
    else:
        new_arr = []
        count = 1
        for i in range(0, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                new_arr.append(count)
                count = 1
        new_arr.append(count)
    return recur_func(new_arr,answer+1)


def solution(arr):
    answer = recur_func(arr,1)
    return answer

print(solution([1,2,3]))


