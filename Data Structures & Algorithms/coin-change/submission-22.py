class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        def dfs(i, amount):
            if amount == 0:
                return 0
            
            if i == len(coins):
                return float('inf')
            
            if (i, amount) in memo:
                return memo[(i, amount)]

            # skip coin
            res = dfs(i + 1, amount)

            # use current coin
            if amount - coins[i] >= 0:
                res = min(res, 1 + dfs(i, amount - coins[i]))
            
            memo[(i, amount)] = res
            return res

        return dfs(0, amount) if dfs(0, amount) != float('inf') else -1