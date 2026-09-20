class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [0] * 26
        tArr = [0] * 26

        for c in s:
            charIndex = ord(c) - ord('a')
            sArr[charIndex] += 1

        for c in t:
            charIndex = ord(c) - ord('a')
            tArr[charIndex] += 1

        return sArr == tArr
        

        
        