class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def climb(i):
            if i >= n:
                return 0

            return cost[i] + min(climb(i + 1), climb(i + 2))
        
        return min(climb(0), climb(1))