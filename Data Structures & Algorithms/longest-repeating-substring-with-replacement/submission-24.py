class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        counts = {}

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            max_count = max(counts.values())
            window_size = r - l + 1
            num_replacements = window_size - max_count
            while num_replacements > k:
                counts[s[l]] -= 1
                l += 1
                max_count = max(counts.values())
                window_size = r - l + 1
                num_replacements = window_size - max_count
            
            res = max(res, r - l + 1)
        
        return res