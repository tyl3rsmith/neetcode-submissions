class Solution:
    def coinChange(self, coins, amount):
        memo = [-1] * (amount + 1)
        def dfs(curr):
            if curr == amount:
                return 0

            if memo[curr] != -1:
                return memo[curr]
            
            res = float('inf')
            for c in coins:
                if curr + c <= amount:
                    res = min(res, 1 + dfs(curr + c))
            
            memo[curr] = res
            return res
        
        res = dfs(0)
        return -1 if res >= float('inf') else res

