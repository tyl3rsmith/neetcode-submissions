class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] > prices[r]: # negative profit, found better day to buy low
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                r += 1
        
        return maxP