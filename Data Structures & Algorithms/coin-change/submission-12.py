class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # no coin will take amount + 1, if its still this it was impossible to make change for so return -1
        dp[0] = 0 # base case: amount 0 requires 0 coins

        for c in coins:
            if c <= amount:
                dp[c] = 1

        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return -1 if dp[amount] == amount + 1 else dp[amount]