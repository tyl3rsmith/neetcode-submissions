class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # subproblem: dp[i] = max sum we can get if we end at i

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)