class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # subproblem: if equal, get lcs of remainder and add 1
        # subproblem: if not equal shift one at a time and get the max lcs
        # base case: lcs of empty strings is 0

        # text1: rows, text2: cols

        memo = {} # (i, j) -> result

        def dfs(i, j):
            if i == len(text1):
                return 0
            
            if j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if text1[i] == text2[j]:
                res = max(res, 1 + dfs(i + 1, j + 1))
            else:
                res = max(res, max(dfs(i + 1, j), dfs(i, j + 1)))
            
            memo[(i, j)] = res
            return res

        return dfs(0, 0)
