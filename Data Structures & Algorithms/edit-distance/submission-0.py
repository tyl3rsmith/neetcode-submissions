class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j): 
            # base case: word1 is empty, return remaining length of word2
            if i == m:
                return n - j
            
            # base case: word2 is empty, return remaining length of word1
            if j == n:
                return m - i
            
            # if they are equal we dont need to consider i, j, just shift them
            res = float('inf')
            if word1[i] == word2[j]:
                res = min(res, dfs(i + 1, j + 1))
            
            # insert: shift j assuming j is taken care of by inserting in word1
            choice1 = 1 + dfs(i, j + 1)
            # delete: ignore i, shift i by 1
            choice2 = 1 + dfs(i + 1, j)
            # replace: make i = j but still incur a cost of 1
            choice3 = 1 + dfs(i + 1, j + 1)
            res = min(res, choice1, choice2, choice3)
            
            return res
        
        return dfs(0, 0)

            

            
