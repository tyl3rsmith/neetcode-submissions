class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashtable = [0] * 26

        for i in range(len(s)):
            hashvalS = ord(s[i]) - ord('a')
            hashvalT = ord(t[i]) - ord('a')

            hashtable[hashvalS] += 1
            hashtable[hashvalT] -= 1

        return hashtable == [0] * 26