class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '{}' in s or '()' in s:
            s = self.myReplace(s, '[]', '')
            s = self.myReplace(s, '{}', '')
            s = self.myReplace(s, '()', '')
        
        return s == ''

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
