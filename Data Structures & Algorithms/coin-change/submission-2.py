class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = the minimum number of coins to make amount i
        dp = [float('inf')] * (amount + 1)

        # base case: amount 0 takes 0 coins
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        res = dp[amount]
        return -1 if res >= float('inf') else res