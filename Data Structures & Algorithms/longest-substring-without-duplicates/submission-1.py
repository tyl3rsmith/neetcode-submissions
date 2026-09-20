class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] not in charSet:
                    charSet.add(s[j])
                else:
                    break

            res = max(res, len(charSet))
        
        return res