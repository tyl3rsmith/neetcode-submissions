class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i + j) == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and s3[i + j] == s1[i]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return memo[(i, j)]
            
            if j < len(s2) and s3[i + j] == s2[j]:
                if dfs(i, j + 1):
                    memo[(i, j)] = True
                    return memo[(i, j)]
            
            memo[(i, j)] = False
            return memo[(i, j)]
        
        return dfs(0, 0)