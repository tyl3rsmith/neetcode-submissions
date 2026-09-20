class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1
            
            key = tuple(chars)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return [groups[group] for group in groups]