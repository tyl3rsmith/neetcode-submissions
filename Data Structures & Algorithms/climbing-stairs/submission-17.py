class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top of the staircase i.e. n = the top stair
        # we can climb with either 1 or 2 steps at a time

        dp = [0] * (n + 1) # index n will be the number of distinct ways to reach step n

        # base case: we know there's only 1 way to start at 0
        # and there's only 1 way to get to step 1 from step 0
        dp[0] = 1
        dp[1] = 1

        # recurrence:
        # for future steps, the ways to get from 0 to the ith step is:
        # the sum of the ways to get to the i-1th step from 0 (take 1 step)
        # and the i-2th step from 0 (take 2 steps)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
