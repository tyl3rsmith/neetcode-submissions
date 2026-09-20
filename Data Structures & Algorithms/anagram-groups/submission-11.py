class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {} # sorted str -> list of anagrams

        for word in strs:
            sorted_key = ''.join(sorted(word))
            print(sorted_key)

            if sorted_key in groups:
                groups[sorted_key].append(word)
            else:
                groups[sorted_key] = [word]
        
        for group in groups:
            res.append(groups[group])
        
        return res