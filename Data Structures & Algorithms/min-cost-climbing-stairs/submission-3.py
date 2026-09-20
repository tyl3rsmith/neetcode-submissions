class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from the i-th floor
        # once we pay the cost we can step to the (i + 1)th or (i + 2)th floor
        # can start at index 0 or index 1

        # return: min cost to reach the top (past last index in cost)

        n = len(cost)
        dp = [0] * (n + 1)
        # base case:
        # dp[0] = dp[1] = 0 since we can start at either position

        # recurrence:
        # the min cost to get to the ith step is
        # the min cost coming from 0 to the i - 1th step or i - 2th step
        # we still need to pay the cost for taking the i - 1th or i - 2th step to reach i
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]

        