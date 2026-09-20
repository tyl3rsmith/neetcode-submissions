class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            # found a valid decoding
            if i == len(s):
                return 1
            
            # invalid decoding exit path early
            if s[i] == '0':
                return 0
            
            # split by the one digit which is nonzero if we got here
            res = dfs(i + 1)

            # split by two digits
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += dfs(i + 2)
            
            return res

        return dfs(0)
        
