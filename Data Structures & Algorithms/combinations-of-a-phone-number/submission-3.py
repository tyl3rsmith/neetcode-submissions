class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        table = {"2": "abc", "3": "def", "4": 'ghi', "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return

            for c in table[digits[i]]:
                curStr += c
                backtrack(i + 1, curStr)
                curStr = curStr[:-1]
        
        if digits:
            backtrack(0, "")
        
        return res