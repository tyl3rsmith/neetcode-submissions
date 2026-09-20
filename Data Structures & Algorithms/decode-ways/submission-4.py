class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }

        def dfs(i):
            # this has been cached or its at the end of the string
            if i in dp:
                return dp[i]
            
            # no ways to decode a string that starts with 0
            if s[i] == '0':
                return 0

            # if its not 0 its between 1-9 so we can decode it
            res = dfs(i + 1)

            # check if we can take 2 digits
            # double digit value must be between 10-26
            if (i + 1 < len(s)):
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                    res += dfs(i + 2)

            dp[i] = res
            return res
        
        return dfs(0)
            