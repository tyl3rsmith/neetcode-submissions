class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        reversedStr = ''
        for c in newStr:
            reversedStr = c + reversedStr
        
        return newStr == reversedStr