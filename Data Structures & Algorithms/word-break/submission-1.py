class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            # we made it to the end
            if i == len(s):
                return True

            # try every word in wordDict as a prefix
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        # if this is true we reached the end
                        memo[i] = True
                        return True
            
            # if we're here we didnt there was a spot where none of the words worked
            memo[i] = False
            return False
        
        return dfs(0)
            

        