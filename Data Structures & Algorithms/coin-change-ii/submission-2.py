class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1 for _ in range(len(coins))] for _ in range(amount + 1)]

        def dfs(amount, i):
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            
            if memo[amount][i] != -1:
                return memo[amount][i]
            
            res = 0
            
            # pick nums[i] as much as we can
            if amount - coins[i] >= 0:
                res += dfs(amount - coins[i], i)
            
            # skip it
            res += dfs(amount, i + 1)
            
            memo[amount][i] = res
            return memo[amount][i]

        return dfs(amount, 0)
            
        