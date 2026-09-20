class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if total == amount:
                return 1
            
            if i >= len(coins):
                return 0
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            res = 0

            if total + coins[i] <= amount:
                res += dfs(i, total + coins[i]) # pick coins[i] as much as possible
            
            res += dfs(i + 1, total) # skip coins[i]
            
            memo[(i, total)] = res
            return memo[(i, total)]
        
        return dfs(0, 0)