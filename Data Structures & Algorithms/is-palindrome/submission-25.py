class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            newStr += c.lower() if self.isAlnum(c) else ''
        
        return newStr == newStr[::-1]
    
    def isAlnum(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9') or
                ord('A') <= ord(s) <= ord('Z'))
        

