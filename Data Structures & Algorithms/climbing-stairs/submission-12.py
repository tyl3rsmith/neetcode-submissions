class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        # bottom-up dp
        # sub problems: ways to get from the nth step to the n - 1 th and n - 2 th step i.e we start at n work our way down

        dp = [0] * (n + 1)

        # base case: only one way to start on n and to get to n-1 from n
        dp[n] = 1
        dp[n - 1] = 1

        # recurrence relation: the number of ways to get from n to
        # the ith step is the sum of the ways of getting from n to the
        # i+1th step and i+2th step which is previously computed in the dp array
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]


