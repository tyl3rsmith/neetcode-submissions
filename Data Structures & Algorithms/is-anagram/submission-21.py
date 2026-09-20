class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for c in s:
            if c in sMap:
                sMap[c] += 1
            else:
                sMap[c] = 1

        
        for c in t:
            if c in tMap:
                tMap[c] += 1
            else:
                tMap[c] = 1
            
        
        for k in sMap:
            if k not in tMap:
                return False
            
            if sMap[k] != tMap[k]:
                return False
        
        return True
            
            
        