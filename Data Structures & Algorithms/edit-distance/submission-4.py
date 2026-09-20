class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
           #insert = 1 + dfs(i, j + 1)
            #delete = 1 + dfs(i + 1, j)
            #replace = dfs(i + 1, j + 1) if word1[i] == word2[j] else 1 + dfs(i + 1, j + 1)
        
        m, n = len(word1), len(word2)
        # base case: empty word1 and word2 requires 0 moves
        # subproblem: dp[i][j] = min moves to convert word1[i:] into word2[j:]
        # m rows, n cols
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # base case: last row word1 is empty but word2 exists
        for i in range(n - 1, -1, -1):
            dp[m][i] = n - i
        
        # base case: last col word2 is empty but word1 exists
        for j in range(m - 1, -1, -1):
            dp[j][n] = m - j
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                insert = 1 + dp[i][j + 1]
                delete = 1 + dp[i + 1][j]
                replace = dp[i + 1][j + 1] if word1[i] == word2[j] else 1 + dp[i + 1][j + 1]
                dp[i][j] = min(insert, delete, replace)
        
        for row in dp:
            print(row)


        return dp[0][0]

       