class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        buy_day = 0
        sell_day = 0

        for i in range(len(prices)):
            sell_day = i

            if prices[sell_day] < prices[buy_day]:
                # negative profit buy this day instead
                buy_day = i
            else:
                # positive profit
                res = max(res, prices[sell_day] - prices[buy_day])

        return res

