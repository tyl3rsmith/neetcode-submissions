class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts[s[r]])
            num_replacements = (r - l + 1) - maxf

            while num_replacements > k:
                counts[s[l]] -= 1
                l += 1

                maxf = max(maxf, counts[s[l]])
                num_replacements = (r - l + 1) - maxf
            
            res = max(res, r - l + 1)
        
        return res



