class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        dp = [0] * (n + 1)

        # base cases:
        dp[0] = 1 # only 1 way to start at step 0
        dp[1] = 1 # only 1 way to get from step 0 to step 1

        # recurrence: the i-th step is dependent on the 2 before it
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


