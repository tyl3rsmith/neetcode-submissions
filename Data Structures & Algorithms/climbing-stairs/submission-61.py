class Solution:
    def climbStairs(self, n: int) -> int:
        dp1 = dp2 = 1
        for i in range(2, n + 1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2