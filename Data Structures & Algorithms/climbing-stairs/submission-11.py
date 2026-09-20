class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        # bottom-up dp

        dp = [0] * (n + 1) # [0, 0, 1, 1]
        dp[n] = 1
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
    
        return dp[0]

