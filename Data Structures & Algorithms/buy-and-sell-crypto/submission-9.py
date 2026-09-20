class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0 # we are buying on day l
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                if prices[r] < prices[l]:
                    l = r
            
            res = max(res, profit)

        return res