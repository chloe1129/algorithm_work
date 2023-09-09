class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        widx = 0
        for i in nums:
            if i != 0:
                nums[widx] = i
                widx+=1
        for j in range(widx,len(nums)):
            nums[j]=0

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
        