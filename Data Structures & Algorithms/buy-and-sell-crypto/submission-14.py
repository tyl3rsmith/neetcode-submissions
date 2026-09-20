class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]

            if sell - buy > 0:
                maxProfit = max(maxProfit, sell - buy)
            
            if sell < buy:
                buy = sell
        
        return maxProfit