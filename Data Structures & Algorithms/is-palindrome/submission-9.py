class Solution:
    def is_alnum(self, c) -> bool:
        return ord(c) in range(ord('a'), ord('z') + 1) or ord(c) in range(ord('0'), ord('9') + 1)

    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for c in s.lower():
            if self.is_alnum(c):
                new_str += c
        
        return new_str == new_str[::-1]