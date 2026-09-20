class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            if sell > buy:
                maxProfit = max(maxProfit, sell - buy)
            
            if sell < buy:
                l = r
            
            r += 1
        
        return maxProfit
