class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price of neetcoin on ith day
        # can make as many transactions
        # cant sell then buy on the next day (cooldown of 1 day after selling)
        # we must sell the stock before we buy again

        buying = True
        selling = False

        def dfs(i, state):
            # base case: profit of an empty array is 0
            if i >= len(prices):
                return 0
            
            # choice 1: take a cooldown
            cooldown = dfs(i + 1, state)

            if state == buying:
                buy = dfs(i + 1, selling) - prices[i]
                return max(buy, cooldown)
            
            if state == selling:
                sell = dfs(i + 2, buying) + prices[i]
                return max(sell, cooldown)

        return dfs(0, buying)