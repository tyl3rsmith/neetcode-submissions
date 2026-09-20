class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                    
                stack.pop()
                
        
        return len(stack) == 0