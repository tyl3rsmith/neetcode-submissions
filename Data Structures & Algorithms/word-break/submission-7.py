class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            # at every step try every word
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return memo[i]
            
            # if we got here no words were able to be used to split
            memo[i] = False
            return memo[i]
        
        return dfs(0)
        