class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        counts = {}

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)

        return res


