class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    if j - i + 1 > resLen:
                        res = s[i : j + 1]
                        resLen = j - i + 1
                               
        return res
