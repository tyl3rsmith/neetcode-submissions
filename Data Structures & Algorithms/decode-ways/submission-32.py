class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp1 = 1
        dp2 = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp3 = 0
            else:
                dp3 = dp1

                if i + 1 < n and ((s[i] == '1') or (s[i] == '2' and s[i + 1] in '0123456')):
                    dp3 += dp2
            
            dp1, dp2 = dp3, dp1
        
        return dp1