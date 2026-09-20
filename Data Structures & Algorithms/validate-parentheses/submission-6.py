class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in close_to_open:
                if not stack:
                    return False
                prev = stack.pop()
                if close_to_open[c] != prev:
                    return False
            else:
                stack.append(c)

        return True if not stack else False       
