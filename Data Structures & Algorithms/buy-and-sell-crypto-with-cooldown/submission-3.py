class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of neetcoin on ith day
        # can make as many transactions
        # cant sell then buy on the next day (cooldown of 1 day after selling)
        # we must sell the stock before we buy again

        # buy, sell, or cooldown
        # initially start as buying, we can always choose to do a cooldown regardless

        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            # cooldown
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else: 
                sell = dfs(i + 2, True) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]

        return dfs(0, True)