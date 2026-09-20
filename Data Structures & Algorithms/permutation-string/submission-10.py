class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = {}
        for c in s1:
            if c in s1_map:
                s1_map[c] += 1
            else:
                s1_map[c] = 1
        
        s2_map = {}
        for i in range(len(s1)):
            if s2[i] in s2_map:
                s2_map[s2[i]] += 1
            else:
                s2_map[s2[i]] = 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            print(s2_map)
            if s1_map == s2_map:
                return True
            
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]

            l += 1
            if s2[r] in s2_map:
                s2_map[s2[r]] += 1
            else:
                s2_map[s2[r]] = 1
        
        return s1_map == s2_map

        