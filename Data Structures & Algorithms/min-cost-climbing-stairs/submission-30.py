class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = 0 # i + 1 floor
        dp2 = 0 # i + 2 floor

        # base case: top floors at last 2 indices require 0 to get to starting from there

        for i in range(len(cost) - 1, -1, -1):
            dp1, dp2 = cost[i] + min(dp1, dp2), dp1
        
        return min(dp1, dp2)