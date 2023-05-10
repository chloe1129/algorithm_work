def solution(nums):
    if len(set(nums))>len(nums)//2:
        return len(nums)//2
    else:
        return len(set(nums))
print(solution([3,3,3,2,2,4]))