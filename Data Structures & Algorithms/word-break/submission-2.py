class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * (len(s) + 1)
        def dfs(i):
            if memo[i] != -1:
                return True if memo[i] == 1 else False
                
            # we made it to the end
            if i == len(s):
                return True

            # try every word in wordDict as a prefix
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        # if this is true we reached the end
                        memo[i] = 1
                        return True
            
            # if we're here we didnt there was a spot where none of the words worked
            memo[i] = 0
            return False
        
        return dfs(0)
            

        