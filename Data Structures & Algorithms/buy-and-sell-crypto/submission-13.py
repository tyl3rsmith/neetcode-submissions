class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                buy = prices[i]
                sell = prices[j]
                
                if sell - buy > 0:
                    maxProfit = max(maxProfit, sell - buy)
        
        return maxProfit