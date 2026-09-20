class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from the i-th floor
        # once we pay the cost we can step to the (i + 1)th or (i + 2)th floor
        # can start at index 0 or index 1

        # return: min cost to reach the top (past last index in cost)

        # space saving approach


        n = len(cost)

        one, two = cost[n - 2], cost[n - 1]

        # cost[i] stores the min cost to get from stair i to the top
        for i in range(n - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        
        return min(one, two)
            



        