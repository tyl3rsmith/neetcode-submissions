class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_Map, t_Map = [0] * 26, [0] * 26

        for c in s:
            s_Map[ord(c) - ord('a')] += 1
        
        for c in t:
            t_Map[ord(c) - ord('a')] += 1
        
        print(s_Map)
        print(t_Map)
            
        for i in range(26):
            if s_Map[i] != t_Map[i]:
                return False
        
        return True
        