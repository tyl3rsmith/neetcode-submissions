class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        # hash into buckets
        # the key will be the character counts

        for s in strs:

            # frequency of each character in s
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            # use this as a key to group strings with same frequency
            key = tuple(freq)
            if key in groups: # same freq detected these are anagrams
                groups[key].append(s)
            else:
                groups[key] = [s]

            
        
        return [x for x in groups.values()]
            


        