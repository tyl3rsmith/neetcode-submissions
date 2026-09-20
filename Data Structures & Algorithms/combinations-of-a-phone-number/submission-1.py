class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        table = {"2": "abc", "3": "def", "4": 'ghi', "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for letter in table[digits[i]]:
                dfs(i + 1, curStr + letter)
        
        if digits:
            dfs(0, "")
        
        return res

        