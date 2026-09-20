class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one
        
        return one




