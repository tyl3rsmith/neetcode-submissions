class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 1)]
        

        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = -prices[i] + dp[i + 1][1]
                    cooldown = dp[i + 1][0]
                    dp[i][0] = max(buy, cooldown)
                else:
                    sell = prices[i] + dp[i + 2][0] if i + 2 < len(prices) else prices[i]
                    cooldown = dp[i + 1][1]
                    dp[i][1] = max(sell, cooldown)
        
        return dp[i][0]