class Solution:
    def coinChange(self, coins, amount):
        # dp[i] = min number of ways to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # base case 0 coins needed to make amount 0

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0: # try each valid coin update with min required
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return dp[-1] if dp[-1] != float('inf') else -1
