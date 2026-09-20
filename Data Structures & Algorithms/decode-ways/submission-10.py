class Solution:
    def numDecodings(self, s: str) -> int:
        # 121
        # 1
        # 2
        # 1
        memo = {}
        def dfs(i):
            # if we reach the end it was a valid decoding
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]
                
            # choose 1 character
            res = dfs(i + 1)
            
            # choose 2 characters
            if (i < len(s) - 1):
                if (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                    res += dfs(i + 2)

            memo[i] = res
            return memo[i]
            
        return dfs(0)