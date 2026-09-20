class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = [0] * 26

        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')

            count[s_index] += 1
            count[t_index] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True
        
        