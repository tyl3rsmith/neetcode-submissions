class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for i in range(n - 1, -1, -1):
            nextDP = [0 for _ in range(amount + 1)]
            nextDP[0] = 1

            for amt in range(1, amount + 1):
                # skip this coin
                nextDP[amt] = dp[amt]

                # use this coin
                if amt - coins[i] >= 0:
                    nextDP[amt] += nextDP[amt - coins[i]]

            dp = nextDP
        return dp[amount]