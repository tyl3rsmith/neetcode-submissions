class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append(''.join(s))
            
            if open_count < n:
                s.append('(')
                backtrack(open_count + 1, closed_count)
                s.pop()
            
            if closed_count < open_count:
                s.append(')')
                backtrack(open_count, closed_count + 1)
                s.pop()
        
        backtrack(0, 0)
        return res

        