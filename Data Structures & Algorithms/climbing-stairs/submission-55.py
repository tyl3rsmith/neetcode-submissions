class Solution:
    def climbStairs(self, n: int) -> int:
        dp1 = 1 # i + 1
        dp2 = 1 # i + 2

        for i in range(n - 1):
            dp1, dp2 = dp1 + dp2, dp1
        
        return dp1