class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        dp1 = 1
        dp2 = 1

        for i in range(n - 2, -1, -1):
            dp1, dp2 = dp1 + dp2, dp1

        return dp1

