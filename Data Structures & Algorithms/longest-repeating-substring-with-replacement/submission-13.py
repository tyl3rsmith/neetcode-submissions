class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        res = 0

        counts = {}
        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            if counts[s[r]] > maxf:
                maxf = counts[s[r]]

            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                if counts[s[r]] > maxf:
                    maxf = counts[s[r]]
                l += 1

            res = max(res, (r - l + 1))
        
        return res

        
        