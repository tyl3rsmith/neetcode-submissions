class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(n):
            if n <= 2:
                return n
            
            if n in memo:
                return memo[n]

            climb1 = climb(n - 1)
            climb2 = climb(n - 2)

            memo[n] = climb1 + climb2
            return climb1 + climb2
        
        return climb(n)