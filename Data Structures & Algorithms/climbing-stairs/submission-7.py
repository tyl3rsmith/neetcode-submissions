class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(x):
            if x >= n:
                if x == n:
                    return 1
                else:
                    return 0
            
            return climb(x + 1) + climb(x + 2)
        
        return climb(0)