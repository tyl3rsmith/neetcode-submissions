class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {} # sorted str and original str
        res = []

        for i in range(0, len(strs)):
            sorted_elem = "".join(sorted(strs[i]))
            if (sorted_elem not in sorted_strs):
                sorted_strs[sorted_elem] = [strs[i]]
            else:
                sorted_strs[sorted_elem].append(strs[i])

        for key in sorted_strs:
            res.append(sorted_strs[key])

        return res
        