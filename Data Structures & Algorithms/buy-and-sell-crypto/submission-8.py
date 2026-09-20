class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            if profit > 0:
                res = max(res, profit)
            elif profit < 0:
                l = r
        
        return res