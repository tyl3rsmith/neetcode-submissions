class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            res = float('inf')
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            
            memo[amount] = res
            return res
        
        res = dfs(amount)
        return -1 if res >= float('inf') else res

