class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = res = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            
            res = max(res, prices[sell] - prices[buy])
        return res


