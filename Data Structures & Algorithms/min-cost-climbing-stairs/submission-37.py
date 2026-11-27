class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}

        def climb(i):
            if i >= n:
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return cache[i]

        return min(climb(0), climb(1))

