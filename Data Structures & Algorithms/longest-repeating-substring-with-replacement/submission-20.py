class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        # brute force check every sub string
        for i in range(len(s)):
            count, maxf = {}, 0

            # for each one count chars and keep track of the max
            for j in range(i, len(s)):
                if s[j] in count:
                    count[s[j]] += 1
                else:
                    count[s[j]] = 1

                maxf = max(maxf, count[s[j]])
                
                # if this is a valid window update res
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
                else:
                    break
        
        return res