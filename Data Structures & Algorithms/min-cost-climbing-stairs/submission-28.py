class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        def climb(i):
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return cache[i]
        
        return min(climb(0), climb(1))