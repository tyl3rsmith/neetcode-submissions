class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in range(len(s)):
            if s[i] not in char_map:
                stack.append(s[i])
            else: # s[i] in char_map
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != char_map[s[i]]:
                    return False

        return len(stack) == 0


            

        