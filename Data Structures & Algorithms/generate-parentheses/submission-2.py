class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def isValid(s):
            if s[0] == ')':
                return False

            num_open = 0
            num_closed = 0
            for c in s:
                if c == '(':
                    num_open += 1
                else:
                    num_closed += 1
                
                if num_closed > num_open:
                    return False
                
            return num_open == num_closed

        def dfs(s):
            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs('')
        return res
        