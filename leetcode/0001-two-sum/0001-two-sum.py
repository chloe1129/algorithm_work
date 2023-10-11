class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i =1
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hashmap:
                return [i, hashmap[c]]
        
            hashmap[nums[i]]=i