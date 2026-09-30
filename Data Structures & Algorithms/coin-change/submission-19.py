class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1) # min coins to make amount i
        dp[0] = 0 # base case: 0 coins needed to make amount 0

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        
        return dp[-1] if dp[-1] != amount + 1 else -1
