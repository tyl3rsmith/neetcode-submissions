class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count1 = {}
        for c in s1:
            count1[c] =  count1[c] + 1 if c in count1 else 1
        
        print(count1)
        
        for i in range(len(s2)):
            count2 = {}
            cur = 0
            need = len(count1)
            for j in range(i, len(s2)):
                count2[s2[j]] = count2[s2[j]] + 1 if s2[j] in count2 else 1

                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                
                if cur == need:
                    return True
        
        return False
