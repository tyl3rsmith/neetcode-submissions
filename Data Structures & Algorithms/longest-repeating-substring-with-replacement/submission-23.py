class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        counts = {}
        maxC = 0

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            
            maxC = max(maxC, counts[s[r]])

            while (r - l + 1) - maxC > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res