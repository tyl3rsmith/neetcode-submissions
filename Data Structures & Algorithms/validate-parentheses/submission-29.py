class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                # make sure its not just a close paren or a mismatched one
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                
                stack.pop()
        
        # make sure its not just open parens
        return len(stack) == 0
