class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        left = 0
        right = len(nums)-1
        while(left<right):
            p = (left+right)//2
            if nums[p]<nums[p+1]:
                left = p+1
            elif nums[p]>nums[p+1]:
                right = p
        return left