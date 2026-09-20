class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i = j = 0
        # i: iterates over s
        # j: iterates over t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        # if i got to the end we know s is a subsequence
        # if j got to the end and i didnt its not a subsequence
        return i == len(s)
        