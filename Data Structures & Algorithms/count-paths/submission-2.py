class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if i > m - 1 or j > n - 1:
                return 0

            return dfs(i + 1, j) + dfs(i, j + 1) 
        
        return dfs(0, 0)
