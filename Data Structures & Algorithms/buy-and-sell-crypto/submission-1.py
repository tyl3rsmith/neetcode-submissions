class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l = buy, r = sell
        res = 0

        while r < len(prices):
            if prices[l] > prices[r]: # found a cheaper day to buy
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r += 1
        
        return res
