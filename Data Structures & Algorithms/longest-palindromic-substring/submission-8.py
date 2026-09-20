class Solution:    
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    if (j - i + 1) > resLen:
                        resLen = j - i + 1
                        resIdx = i


        return s[resIdx:resIdx + resLen]