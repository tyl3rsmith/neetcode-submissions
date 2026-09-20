class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts1, counts2 = {}, {}
        for i in range(len(s1)):
            if s1[i] in counts1:
                counts1[s1[i]] += 1
            else:
                counts1[s1[i]] = 1
            
            if s2[i] in counts2:
                counts2[s2[i]] += 1
            else:
                counts2[s2[i]] = 1
        
        if counts1 == counts2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            
            if s2[r] in counts2:
                counts2[s2[r]] += 1
            else:
                counts2[s2[r]] = 1
            
            if counts1 == counts2:
                return True

            l += 1
        
        return False

        
        


        
                
