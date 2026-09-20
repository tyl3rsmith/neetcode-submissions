class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = res = 0

        for r in range(len(prices)):
            buy = prices[l]
            sell = prices[r]

            profit = sell - buy

            if profit < 0:
                l = r
            else:
                res = max(res, profit)

        return res