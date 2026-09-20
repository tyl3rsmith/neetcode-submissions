class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        soln = []
        res = []

        def backtrack(num_open, num_closed):
            if num_open == n and num_closed == n: # base case found a sol-n
                res.append("".join(soln))
            
            if num_open < n:
                soln.append('(')
                backtrack(num_open + 1, num_closed)
                soln.pop()
            
            if num_closed < num_open:
                soln.append(')')
                backtrack(num_open, num_closed + 1)
                soln.pop()
            
        backtrack(0, 0)
        return res