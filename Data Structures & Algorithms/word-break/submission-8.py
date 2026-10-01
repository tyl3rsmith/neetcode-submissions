class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            
            if i in memo:
                return memo[i]

            # try to fit each word into the string
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
        
            # none of the words fit into the string
            memo[i] = False
            return False

        return dfs(0)



        