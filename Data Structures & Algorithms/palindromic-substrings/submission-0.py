class Solution:
    def countSubstrings(self, s: str) -> int:
        res, n = 0, len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    res += 1
        
        return res    