class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        table = {"2": "abc", "3": "def", "4": 'ghi', "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(i):
            if not digits:
                return
                
            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return
            
            for letter in table[digits[i]]:
                curr.append(letter)
                dfs(i + 1)
                curr.pop()
        
        dfs(0)
        return res

        