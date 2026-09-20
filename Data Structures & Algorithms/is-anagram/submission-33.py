class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = [0] * 26

        for c in s:
            hashtable[ord(c) - ord('a')] += 1
        
        for c in t:
            hashtable[ord(c) - ord('a')] -= 1
        
        return hashtable == [0] * 26
