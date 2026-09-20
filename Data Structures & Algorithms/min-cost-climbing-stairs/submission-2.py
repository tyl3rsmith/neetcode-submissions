class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking a step from the i-th floor
        # once we pay the cost we can step to the (i + 1)th or (i + 2)th floor
        # can start at index 0 or index 1

        # return: min cost to reach the top (past last index in cost)

        n = len(cost)
        memo = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
                
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        
        return min(dfs(0), dfs(1))

        