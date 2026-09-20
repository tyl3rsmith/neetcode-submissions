class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        res = []

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in table:
                table[tuple(count)].append(s)
            else:
                table[tuple(count)] = [s]

        for key in table:
            res.append(table[key])
        
        return res

        