class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
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
            
        for key in s_Map:
            if key not in t_Map:
                return False
            if s_Map[key] != t_Map[key]:
                return False
        
        return True
        