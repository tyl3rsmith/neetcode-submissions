class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # price[i] price of neet coin on the ith day
        # cooldown of 1 day to buy after you sell
        # can only have at most one coin at a time

        # at each point we can either buy or skip
        # i: index we are processing, j: index of the last one we bought

        # skip: dfs(i + 1, j)
        # buy: dfs(i + 1, i)

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            # choice 1 don't buy neetcoin
            cooldown = dfs(i + 1, buying)

            # choice 2: buy neetcoin only if buying is True
            if buying:
                buy = -prices[i] + dfs(i + 1, not buying)
                return max(buy, cooldown)
            else:
            # we are selling
                sell = prices[i] + dfs(i + 2, not buying)
                return max(sell, cooldown)

        return dfs(0, True)
        