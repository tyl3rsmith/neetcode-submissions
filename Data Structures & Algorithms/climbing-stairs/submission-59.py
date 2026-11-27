class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        cache[0] = 1
        cache[1] = 1

        def climb(i):
            if i == 0 or i == 1:
                return cache[i]
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = climb(i - 1) + climb(i - 2)
            return cache[i]
        
        return climb(n)