class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (not s):
            return 0

        charSet = set()
        charSet.add(s[0])
        res = 1
        
        l, r = 0, 1
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res
            
        