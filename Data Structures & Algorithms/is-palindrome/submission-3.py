class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse the string and compare it to the original
        sentence = ""
        for c in s:
            if c.isalnum():
                sentence += c.lower()
        
        return sentence == sentence[::-1]


                