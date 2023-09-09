class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=sum(nums)
        pivot = 0
        for i in range(0,len(nums)):
            num = nums[i]
            rightsum -= num
            leftsum += pivot
            if leftsum == rightsum:
                return i
            pivot = num
        return -1
        
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))