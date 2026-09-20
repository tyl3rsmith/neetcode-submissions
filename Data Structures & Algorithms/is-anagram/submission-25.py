class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Map, t_Map = {}, {}

        for c in s:
            if c in s_Map:
                s_Map[c] += 1
            else:
                s_Map[c] = 1
        
        for c in t:
            if c in t_Map:
                t_Map[c] += 1
            else:
                t_Map[c] = 1
            
        return t_Map == s_Map
        