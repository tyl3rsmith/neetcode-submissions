class Solution:
    def isValid(self, s: str) -> bool:
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
