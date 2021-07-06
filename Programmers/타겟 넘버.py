def solution(numbers, target):
    nums = [0,0]
    targets = []
    for i in range(len(numbers)):
        for _ in range(2**i):
            nums.append(numbers[i])
            nums.append(-numbers[i])

    def dfs(i, num = 0):
        if i >= len(nums):
            targets.append(num)
        else:
            num += nums[i]
            dfs(2*i,num)
            dfs(2*i+1,num)

    dfs(1)

    return targets.count(target)//2  
    ## 마지막 재귀 단계에서 append()가 두 번 일어나기 때문에 개수를 2로 나눠줘야 됨.

print(solution([1, 1, 1, 1, 1],	3))