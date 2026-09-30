class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming
        # dp[i][j] = True if s[i:j] is a palindrome
        # s[i:j] is a palindrome when dp[i + 1][j - 1] is a palindrome and s[i] == s[j]

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        resIdx = resLen = 0
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        resIdx = i


        return s[resIdx : resIdx + resLen]
        
            
