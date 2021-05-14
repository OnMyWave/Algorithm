
def solution(nums):
    N = len(nums)/2
    set_nums = set(nums)
    if N>= len(set(nums)):
        return len(set(nums))
    else:
        return N