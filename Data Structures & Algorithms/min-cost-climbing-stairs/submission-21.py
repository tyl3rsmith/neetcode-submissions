class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp1, dp2 = cost[n - 2], cost[n - 1]
        for i in range(n - 3, -1, -1):
            dp1, dp2 = cost[i] + min(dp1, dp2), dp1
        
        return min(dp1, dp2)