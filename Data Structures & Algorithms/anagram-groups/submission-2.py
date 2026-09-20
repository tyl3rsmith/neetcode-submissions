class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        res = []

        for word in strs:
            key = "".join(sorted(word))
            if key in table:
                table[key].append(word)
            else:
                table[key] = [word]
        
        for key in table:
            res.append(table[key])

        return res




        