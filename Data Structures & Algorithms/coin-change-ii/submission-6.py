class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # at each point we have 2 choices
        # pick coins[i] if it doesnt exceed amount
        # skip coins[i] regardless of amount
        # base case: if we reach amount return 1, if we exceed bounds return 0

        memo = {}
        def dfs(i, total):
            if total == amount:
                return 1

            if i >= len(coins):
                return 0
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            res = 0

            # buy
            if total + coins[i] <= amount:
                res += dfs(i, total + coins[i])
            
            # skip
            res += dfs(i + 1, total)

            memo[(i, total)] = res
            return memo[(i, total)]
            
        
        return dfs(0, 0)

        