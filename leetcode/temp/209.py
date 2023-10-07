class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums) < target:
            return 0

        tmp, left, ans = 0, 0, len(nums)

        for right, n in enumerate(nums):
            print('1111111111', left, right, n)
            tmp += n
            print('2222222222', left, right, tmp)
            while tmp >= target:
                print('3333333333', left, right, tmp, nums[left])
                tmp -= nums[left]
                print('4444444444--', left, right, tmp, right-left+1)
                ans = min(ans, right - left + 1)
                left += 1

        return ans


s = Solution()
# print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
# print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
