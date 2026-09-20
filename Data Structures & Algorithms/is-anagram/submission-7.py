class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = {}

        for char in s:
            if char in char_count_s:
                char_count_s[char] += 1
            else:
                char_count_s[char] = 1
        
        for char in t:
            if char in char_count_s:
                char_count_s[char] -= 1
            else:
                return False # if the char is not in the char_count_s then they can't be anagrams
        
        for key in char_count_s:
            if char_count_s[key] != 0:
                return False
        
        return True
