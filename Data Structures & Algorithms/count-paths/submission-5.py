class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # out of bounds values are 0 (row m, col n)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]
