class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
            
        prev, curr = 1, 1

        for i in range(n - 1):
            curr, prev = curr + prev, curr
        
        return curr