class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def climb(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = climb(i + 1) + climb(i + 2)
            return memo[i]
        
        return climb(0)
