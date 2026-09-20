class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            # we read all characters, this decoding is valid
            if i == len(s):
                return 1
            
            # leading 0s are invalid
            if s[i] == '0':
                return 0
            
            # memoization, reduce repeated work
            if i in memo:
                return memo[i]

            # take one digit always allowed
            res = dfs(i + 1)

            # take two digits
            # allowed only if the first digit is 1 or
            # the first digit is 2 and the second is 0-6
            if i + 1 < len(s):
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                    res += dfs(i + 2)

            memo[i] = res
            return memo[i]
        
        return dfs(0)