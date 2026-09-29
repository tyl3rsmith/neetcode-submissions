class Solution:
    def rob(self, nums: List[int]) -> int:
        # choice 1: rob house[i]
        # choice 2: get max we can rob skipping house[i]

        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])

        for i in range(2, n):
            dp1, dp2 = dp2, max(nums[i] + dp1, dp2)
        
        return dp2