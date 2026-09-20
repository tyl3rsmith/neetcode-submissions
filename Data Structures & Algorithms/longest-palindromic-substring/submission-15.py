class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""

        for i in range(len(s)):
            # expand outward checking for palindromes
            # the center is at index i

            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return res
            
            
