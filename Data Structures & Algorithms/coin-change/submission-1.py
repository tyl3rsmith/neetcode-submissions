class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt in memo:
                return memo[amt]

            # base case: we reached the amount
            if amt == 0:
                return 0
            
            # base case: we overshot the amount
            # this path is invalid
            if amt < 0: 
                return float('inf')

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(amt - coin))
            
            memo[amt] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= float('inf') else minCoins
