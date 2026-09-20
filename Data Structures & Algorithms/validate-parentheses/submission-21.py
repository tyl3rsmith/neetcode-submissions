class Solution:
    def isValid(self, s: str) -> bool:
        oldToNew = {'}': '{', ')': '(', ']': '['}
        stack = []

        for c in s:
            if c not in oldToNew:
                stack.append(c)
            else:
                if stack and oldToNew[c] == stack[-1]:
                    stack.pop()
                else: # stack empty or we have a mismatch
                    return False
        
        return len(stack) == 0

    def myReplace(self, s: str, old: str, new: str):
        i = 0
        res = ""

        while i < len(s):
            if s[i:i+len(old)] == old:
                res += new
                i += len(old)
            else:
                res += s[i]
                i += 1
        
        return res
