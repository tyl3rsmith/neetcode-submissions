class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1

        for i in range(n - 1):
            prev, curr = curr, curr + prev
        
        return curr