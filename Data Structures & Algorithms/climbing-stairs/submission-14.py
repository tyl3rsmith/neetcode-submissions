class Solution:
    def climbStairs(self, n: int) -> int:
        zero, one = 1, 1

        for i in range(n - 1):
            zero, one = one, one + zero
        
        return one