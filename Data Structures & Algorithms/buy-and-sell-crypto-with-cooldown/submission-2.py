class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of neetcoin on ith day
        # can make as many transactions
        # cant sell then buy on the next day (cooldown of 1 day after selling)
        # we must sell the stock before we buy again

        # buy, sell, or cooldown
        # initially start as buying, we can always choose to do a cooldown regardless

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            # cooldown
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                return max(buy, cooldown)
            else: 
                sell = dfs(i + 2, True) + prices[i]
                return max(sell, cooldown)

        return dfs(0, True)