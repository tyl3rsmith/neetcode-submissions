class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 2 1
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            # choose 1 character
            res = dfs(i + 1)

            if i < len(s) - 1:
                if s[i] == '1' or s[i] == '2' and s[i + 1] < '7':
                    # choose 2 characters
                    res += dfs(i + 2)

            return res
        
        return dfs(0)
