class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        groups = {} # freq list -> list of anagrams
        for word in strs:
            group = [0] * 26

            for c in word:
                group[ord(c) - ord('a')] += 1
            
            key = tuple(group)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        

        for group in groups:
            res.append(groups[group])

        return res