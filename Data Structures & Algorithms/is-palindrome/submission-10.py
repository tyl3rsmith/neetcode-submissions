class Solution:
    def is_alnum(self, c) -> bool:
        return ord(c) in range(ord('a'), ord('z') + 1) or ord(c) in range(ord('0'), ord('9') + 1)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while (not self.is_alnum(s[l])) and l < r: # skip past non alnum chars
                l += 1
            while (not self.is_alnum(s[r])) and r > l:
                r -= 1
            if s[l] != s[r]: # compare left and right side
                return False
            l += 1
            r -= 1
        
        return True
        