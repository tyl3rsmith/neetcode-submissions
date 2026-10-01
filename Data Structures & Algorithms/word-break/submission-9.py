class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # memo = {}

        # def dfs(i):
        #     if i == n:
        #         return True
            
        #     if i in memo:
        #         return memo[i]

        #     # try to fit each word into the string
        #     for word in wordDict:
        #         if s[i : i + len(word)] == word:
        #             if dfs(i + len(word)):
        #                 memo[i] = True
        #                 return True
        
        #     # none of the words fit into the string
        #     memo[i] = False
        #     return False

        # return dfs(0)

        # dp[i] = True if the substring s[i:] can be broken into words from wordDict
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True



        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i : i + len(word)] == word:
                    #print(s[i : i + len(word)])
                    if dp[i + len(word)]:
                        dp[i] = dp[i + len(word)]
        #print(dp)
        return dp[0]

        