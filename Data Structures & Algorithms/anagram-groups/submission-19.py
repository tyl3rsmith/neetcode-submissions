class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # sort string
        # hash to bucket where the key is the sorted string
        # return result as a list

        for s in strs:
            key = ''.join(sorted(s))

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return [x for x in groups.values()]
            


        