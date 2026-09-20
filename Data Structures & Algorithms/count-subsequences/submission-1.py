class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        def dfs(i, j):
            if j == len(t): # found an entire subsequence
                return 1
            
            if i == len(s): # i at the end but still chars in j
                return 0
            
            # skip this char i and try to match with the next one
            res = dfs(i + 1, j)

            if s[i] == t[j]: # there was a match so check for the next char in j
                res += dfs(i + 1, j + 1)
            
            return res
        
        return dfs(0, 0)

        