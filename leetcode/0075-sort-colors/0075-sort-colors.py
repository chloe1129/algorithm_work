class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx0 = 0
        idx3 = len(nums)-1
        i = 0
        
        while(i<=idx3):
            if nums[i] == 0:
                nums[idx0],nums[i] =  nums[i], nums[idx0]
                idx0 +=1
                i +=1
            elif nums[i] == 2:
                nums[idx3],nums[i] =  nums[i], nums[idx3]
                idx3-=1
                
            else:
                i+=1
        