class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        brackets = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in '([{':
                charStack.append(char)
            else:
                if not charStack or charStack[-1] != brackets[char]:
                    return False
                
                charStack.pop()
        
        return len(charStack) == 0 # ensure its not only open parentheses and no closing ones




        seen = []
        
        for char in s:
            if char in '([{':
                seen.append(char)
            else:
                if not seen:
                    return False 

                if char == '}' and seen[-1] != '{':
                    return False
                
                if char == ']' and seen[-1] != '[':
                    return False
                
                if char  == ')' and seen[-1] != '(':
                    return False
                
                seen.pop()
        
        return len(seen) == 0
