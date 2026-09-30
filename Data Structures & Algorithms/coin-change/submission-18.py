class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        
        def dfs(amt):
            if amt == 0:
                return 0
            
            if amt in memo:
                return memo[amt]
            
            res = float('inf')
            for c in coins:
                if amt - c >= 0:
                    res = min(res, 1 + dfs(amt - c))
            
            memo[amt] = res
            return res
        
        return -1 if dfs(amount) == float('inf') else dfs(amount)