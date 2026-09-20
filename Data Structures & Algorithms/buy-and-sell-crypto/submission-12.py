class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        profit = 0

        while (r < len(prices)):
            buy = prices[l]
            sell = prices[r]

            if buy > sell:
                l = r
            else:
                profit = max(profit, sell - buy)

            r += 1
        
        return profit
        