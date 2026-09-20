class Solution:
    def isPalindrome(self, s: str) -> bool:
        regular = ""
        for c in s:
            if c.isalnum():
                regular = regular + c.lower()
            
        print(regular)

        reverse_s = ""
        for c in s:
            if c.isalnum():
                reverse_s = c.lower() + reverse_s
        
        return regular == reverse_s
        