class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        # base case: 1 way to make 0
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for amt in range(1, amount + 1):
                dp[i][amt] = dp[i + 1][amt] # skip
                if amt - coins[i] >= 0:
                    dp[i][amt] += dp[i][amt - coins[i]] # use
        
        return dp[0][amount]
