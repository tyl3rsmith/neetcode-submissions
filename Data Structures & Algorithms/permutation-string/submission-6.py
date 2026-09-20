class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map, s2_map = {}, {}
        for i in range(len(s1)):
            if s1[i] in s1_map:
                s1_map[s1[i]] += 1
            elif s1[i] not in s1_map:
                s1_map[s1[i]] = 1
            
            if s2[i] in s2_map:
                s2_map[s2[i]] += 1
            elif s2[i] not in s2_map:
                s2_map[s2[i]] = 1

        l = 0
        for r in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]


            if s2[r] in s2_map:
                s2_map[s2[r]] += 1
            else:
                s2_map[s2[r]] = 1
            
            l += 1

        return s1_map == s2_map
