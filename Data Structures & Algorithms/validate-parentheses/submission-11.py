class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {']': '[', '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in close_to_open: # this is closing 
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else: # stack empty and we got a closing or mismatch parentheses
                    return False
            else: # this is an open
                stack.append(c)
        
        return len(stack) == 0
         
                