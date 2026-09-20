class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        res = 0
        counts = {}

        # sliding window
        for r in range(len(s)):
            # count occurences of each character
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1

            # keep track of the character with max frequency
            # lazily updates but still ensures the correct result
            # makes it less strict on the shrinking condition
            maxf = max(maxf, counts[s[r]])

            # while the window is invalid fix it
            # we know the window is invalid if the number of replacements exceeds k
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1 # this is leaving the window so decrement its count
                l += 1 # shrink the window

            # here the window is valid so potentially could have a larger res
            res = max(res, (r - l + 1)) 
        
        return res

        
        