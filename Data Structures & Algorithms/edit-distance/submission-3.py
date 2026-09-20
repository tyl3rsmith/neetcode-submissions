class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        memo = {}
        def dfs(i, j):
            # word1 is empty
            if i == m:
                return n - j
            
            # word2 is empty
            if j == n:
                return m - i
            
            # already cached
            if (i, j) in memo:
                return memo[(i, j)]

            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = dfs(i + 1, j + 1) if word1[i] == word2[j] else 1 + dfs(i + 1, j + 1)
            
            memo[(i, j)] = min(insert, delete, replace)
            return memo[(i, j)]
        
        return dfs(0, 0)

       