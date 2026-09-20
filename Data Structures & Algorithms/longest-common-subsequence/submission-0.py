class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # subproblem: if equal, get lcs of remainder and add 1
        # subproblem: if not equal shift one at a time and get the max lcs
        # base case: lcs of empty strings is 0

        # text1: rows, text2: cols
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]