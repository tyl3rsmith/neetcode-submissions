class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for c in s:
            if c in countS:
                countS[c] += 1
            else:
                countS[c] = 1
            
        countT = {}
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
        
        return countS == countT
