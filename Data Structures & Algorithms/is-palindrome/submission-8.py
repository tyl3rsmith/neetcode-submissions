class Solution:
    def is_alnum(self, c) -> bool:
        return ord(c) in range(ord('a'), ord('z') + 1) or ord(c) in range(ord('0'), ord('9') + 1)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        l, r = 0, len(s) - 1

        while l < r:
            while (not self.is_alnum(s[l])) and l < r:
                l += 1
            while (not self.is_alnum(s[r])) and l < r:
                r -= 1
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True