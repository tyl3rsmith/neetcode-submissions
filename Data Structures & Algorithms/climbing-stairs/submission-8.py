class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top
        # can take 1 or 2 steps at a time
        # want number of distinct ways to reach the top

        def climb(x):
            # base case
            if x == n:
                return 1
            elif x > n:
                return 0

            return climb(x + 1) + climb(x + 2)
        
        return climb(0)
