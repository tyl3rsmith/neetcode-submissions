class Solution:
    def coinChange(self, coins, amount):
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for i in range(len(coins)):
            dp[i][0] = 0
        
        for i in range(len(coins) - 1, -1, -1):
            for amt in range(amount + 1):
                dp[i][amt] = min(dp[i][amt], dp[i + 1][amt])
                if amt - coins[i] >= 0:
                    dp[i][amt] = min(dp[i][amt], 1 + dp[i][amt - coins[i]])


        return dp[0][amount] if dp[0][amount] != float('inf') else -1
