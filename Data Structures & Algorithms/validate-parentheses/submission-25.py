class Solution:
    def isValid(self, s: str) -> bool:
        # optimized

        # maintain a stack
        # if we see an open parentheses push it onto the stack
        # if we get a closed bracket we will pop from the stack if the top is the corresponding open bracket
        # if they dont match we can return false as its invalid
        # we will return true only after verifying they all matched i.e. the stack is empty

        stack = []
        bracketMap = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in bracketMap:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracketMap[c]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False



