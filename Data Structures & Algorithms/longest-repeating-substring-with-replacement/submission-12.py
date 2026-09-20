class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        maxChar = s[0]
        res = 0

        while (r < len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            if (count[s[r]] > count[maxChar]):
                maxChar = s[r]
            
            while (r - l + 1) - count[maxChar] > k:
                count[s[l]] -= 1
                maxChar = max(count, key=count.get)
                l += 1
            
            
            res = max(res, r - l + 1)
            r += 1

        return res
        