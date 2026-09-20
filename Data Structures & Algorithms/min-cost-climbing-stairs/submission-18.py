class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def climb(i):
            if i >= len(cost):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return memo[i]
        
        return min(climb(0), climb(1))
        