class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        if n == 0:
            return 1
        elif n < 0:
            return 0
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
