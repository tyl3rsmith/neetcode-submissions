class Solution:
    def isPalindrome(self, s: str):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = ""
        resLen = 0

        for i in range(n):
            for j in range(i, n):
                if (self.isPalindrome(s[i:j+1])):
                    if len(s[i:j+1]) > resLen:
                        res = s[i:j+1]
                        resLen = len(s[i:j+1])
        
        return res

        