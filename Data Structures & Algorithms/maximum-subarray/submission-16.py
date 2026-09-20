class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)] 
        dp[n][0] = -1e6
        dp[n][1] = 0

        for i in range(n - 1, -1, -1):
            dp[i][1] = max(0, nums[i] + dp[i + 1][1])
            dp[i][0] = max(dp[i + 1][0], nums[i] + dp[i + 1][1])
        
        return dp[0][0]
        
        def dfs(i, started):
            if i == len(nums):
                return 0 if started else -1e6

            if started:
                return max(0, nums[i] + dfs(i + 1, True))
            
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
        
        return dfs(0, False)

    