class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i ,j = 0,len(nums)-1
        while(i<len(nums)-1):
            if nums[i]>nums[i+1]:
                break
            i+=1
            
        while(j>=0):
            if nums[j]<nums[j-1]:
                break
            j-=1
        print('first',i,j)
        if i == j:
            return 0
        elif j<i:
            return 0
        
        mn = float("inf")
        mx = float("-inf")
        k = i;
        while k <= j :
            mn=min(mn, nums[k])
            mx=max(mx, nums[k])
            k = k + 1
        # print('herehere',mn,mx)
        while i >=0 and nums[i] > mn :
            i = i - 1
        while j < len(nums) and nums[j] < mx :
            j = j + 1
        # print('final',i,j)
        return j-i-1

        
        