class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = dp2 = 0
        n = len(cost)

        for i in range(2, n + 1):
            dp1, dp2 = dp2, min(cost[i - 1] + dp2, cost[i - 2] + dp1)
        
        return dp2
        