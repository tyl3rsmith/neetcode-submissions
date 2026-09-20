class Solution:    
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        # dp[i][j] = True if s from i to j is a palindrome
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # check for palindromes
                # if len <= 3 and the ends match its a palindrome
                # or if the ends 

                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = j - i + 1
                        resIdx = i
        
        return s[resIdx : resIdx + resLen]