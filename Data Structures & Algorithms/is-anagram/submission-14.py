class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for i in range(len(s)):
            # offset from a gives index from 0-25
            s_index, t_index = ord(s[i]) - ord('a'), ord(t[i]) - ord('a')
            counts[s_index] += 1
            counts[t_index] -= 1
        
        for val in counts:
            if val != 0:
                return False
        
        return True