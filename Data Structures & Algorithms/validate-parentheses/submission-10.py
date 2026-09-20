class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {']': '[', '}': '{', ')': '('}
        
        stack = []
        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            elif not stack:
                return False
            elif stack:
                top = stack.pop()
                if top != closeToOpen[s[i]]:
                    return False
        
        return len(stack) == 0
                
                
