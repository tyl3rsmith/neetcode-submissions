class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = [-1] * (n + 1)
        def climb(i):
            if i >= n:
                return 0
                
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return memo[i]
        
        return min(climb(0), climb(1))