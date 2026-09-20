class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        curr, prev = cost[-1], 0

        for i in range(n - 2, -1, -1):
            curr, prev = cost[i] + min(curr, prev), curr
        
        return min(curr, prev)