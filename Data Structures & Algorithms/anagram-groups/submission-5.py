class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        res = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sorted_dict:
                sorted_dict[sorted_word].append(word)
            else:
                sorted_dict[sorted_word] = [word]
            
        for key in sorted_dict:
            res.append(sorted_dict[key])
        
        return res


        