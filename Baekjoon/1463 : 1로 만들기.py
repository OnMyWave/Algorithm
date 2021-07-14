N = int(input())

nums = [0] * (N+1)

for i in range(2,N+1):
    if i%2 : # 홀수
        if i%3 : 
            nums[i] = nums[i-1] + 1
        else:
            nums[i] = min(nums[i-1],nums[int(i/3)])+1
    else:
        if i%3 :
            nums[i] = min(nums[i-1],nums[int(i/2)])+1
        else:
            nums[i] = min(nums[i-1],nums[int(i/3)],nums[int(i/2)])+1

print(nums[-1])
