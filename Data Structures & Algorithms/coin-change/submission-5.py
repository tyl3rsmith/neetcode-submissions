class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount + 1)
        cache[0] = 0

        def dfs(amount):
            if cache[amount] != -1:
                return cache[amount]
            
            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            
            cache[amount] = res
            return res
        
        res = dfs(amount) 
        return res if res != 1e9 else -1