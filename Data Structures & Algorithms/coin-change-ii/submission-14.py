class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][amount] = # ways to make amount using coins[i:]
        # at coin i we can use coin i 0 or more times
        # and any coin after coin i
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for amt in range(1, amount + 1):
                # If we skip coin i, we look at the number of ways to make amt
                # using the next coins.
                dp[i][amt] = dp[i + 1][amt]

                # include this coin if possible
                # If we can afford this coin, we stay on the same row
                # and add the number of ways to make up the remaining amount amt - coins[i].
                if amt - coins[i] >= 0:
                    dp[i][amt] += dp[i][amt - coins[i]]
        
        return dp[0][amount]