class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            word_count = [0] * 26
            
            for i in range(len(word)):
                word_count[ord(word[i]) - ord('a')] += 1

            key = tuple(word_count)
            
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return [groups[group] for group in groups]
        