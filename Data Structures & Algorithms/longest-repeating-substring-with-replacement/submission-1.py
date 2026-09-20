class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                if s[j] in count:
                    count[s[j]] += 1
                else:
                    count[s[j]] = 1

                maxf = max(maxf, count[s[j]])

                num_replacements = (j - i + 1) - maxf
                if num_replacements <= k:
                    res = max(res, j - i + 1)
        
        return res




        