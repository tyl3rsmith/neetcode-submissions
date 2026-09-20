class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            newStr += c.lower() if self.isAlnum(c) else ''
        
        l, r = 0, len(newStr) - 1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlnum(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9') or
                ord('A') <= ord(s) <= ord('Z'))
        

