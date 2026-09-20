class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ']': '[', ')': '('}

        # if its an open push to stack
        # if its a closed check if the one before is the corresponding open one
        # if not return false otherwise we pop from the stack
        # stack should be empty at the end if it was valid

        for c in s:
            if c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return not stack