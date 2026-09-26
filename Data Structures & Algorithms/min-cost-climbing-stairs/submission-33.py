class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[-1]
        prev1 = cost[-2]
        n = len(cost)

        for i in range(n - 3, -1, -1):
            prev1, prev2 = cost[i] + min(prev1, prev2), prev1
            
        return min(prev1, prev2)