class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: # base case, we reach a solution
                res.append("".join(stack))
                return

            if openN < n: # we can add as many ( as long as we have less than n
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN: # we can add as many ) as long as we have more ( present
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        