class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return True
            
            for w in wordDict:
                # found a match explore the next word
                if (i + len(w) <= len(s) and s[i:i + len(w)] == w):
                    # if the word here and the next one match return True
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
                    # if not try a different word
                    else:
                        continue
            
            # there was at least one point where there wasn't any word that matched
            memo[i] = False
            return False

        return dfs(0)