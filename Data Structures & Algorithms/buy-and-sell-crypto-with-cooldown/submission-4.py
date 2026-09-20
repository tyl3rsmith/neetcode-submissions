class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = -prices[i] + dfs(i + 1, False)
                return max(buy, cooldown)
            else:
                sell = prices[i] + dfs(i + 2, True)
                return max(sell, cooldown)

        return dfs(0, True)