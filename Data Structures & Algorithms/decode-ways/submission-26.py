class Solution:
    def numDecodings(self, s: str) -> int:
        dp = 0 # hold the final computed dp value
        dp1 = 1 # holds the base case value
        dp2 = 0 # conditional variable for when we can take two digits = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1

            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp += dp2
            
            dp, dp1, dp2 = 0, dp, dp1
        
        return dp1
