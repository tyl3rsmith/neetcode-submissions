class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuy = prices[0]

        for sell in prices:
            minbuy = min(minbuy, sell)
            maxP = max(maxP, sell - minbuy)
        
        return maxP