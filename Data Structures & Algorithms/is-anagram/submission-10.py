class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map1, char_map2 = {}, {}

        for char in s:
            if char in char_map1:
                char_map1[char] += 1
            else:
                char_map1[char] = 1
        
        for char in t:
            if char in char_map2:
                char_map2[char] += 1
            else:
                char_map2[char] = 1
        
        return char_map1 == char_map2
        
        