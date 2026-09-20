class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def isValid(s):
            num_open = 0
            for c in s:
                if c == '(':
                    num_open += 1
                else:
                    num_open -= 1
                    if num_open < 0:
                        return False
            return num_open == 0

        def dfs(s):
            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs('')
        return res
        