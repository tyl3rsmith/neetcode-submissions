class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            counts = [0] * 26

            for c in word:
                counts[ord(c) - ord('a')] += 1

            key = tuple(counts)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return [groups[key] for key in groups]

        