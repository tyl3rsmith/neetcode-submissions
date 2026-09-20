class Solution:
    def scoreOfString(self, s: str) -> int:
        l = res = 0
        for r in range(1, len(s)):
            res += abs(ord(s[r]) - ord(s[l]))
            l += 1
        
        return res

        