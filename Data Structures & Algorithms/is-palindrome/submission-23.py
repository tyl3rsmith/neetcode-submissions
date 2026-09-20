class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if ord(c) in range(65, 91) or ord(c) in range(97, 123) or ord(c) in range(48, 58):
                newStr += c.lower()
        
        return newStr == newStr[::-1]