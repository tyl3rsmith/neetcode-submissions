class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if j == n:
                return m - i
            
            if i == m:
                return n - j
            
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = dfs(i + 1, j + 1) if word1[i] == word2[j] else 1 + dfs(i + 1, j + 1)

            return min(insert, delete, replace)
        
        return dfs(0, 0)
            

            
