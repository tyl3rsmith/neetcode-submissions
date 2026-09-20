class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c not in char_map:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                prev = stack.pop()
                if prev != char_map[c]:
                    return False

        return len(stack) == 0


            

        