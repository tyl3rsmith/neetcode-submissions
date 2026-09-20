class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in groups:
                groups[tuple(count)].append(s)
            else:
                groups[tuple(count)] = [s]
        
        res = []
        for key in groups:
            res.append(groups[key])
        
        return res