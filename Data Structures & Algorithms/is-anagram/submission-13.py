class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        
        return countT == countS
        