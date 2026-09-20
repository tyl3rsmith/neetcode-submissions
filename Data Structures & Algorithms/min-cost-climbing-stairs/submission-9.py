class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def climb(i):
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]
                
            cache[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return cache[i]
        
        return min(climb(0), climb(1))
        