class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sum(nums)] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for jump in range(nums[i] + 1):
                if i + jump < n:
                    dp[i] = min(dp[i], 1 + dp[i + jump])
        
        return dp[0]


        