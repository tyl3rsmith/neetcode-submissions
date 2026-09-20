class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string count the frequencies of characters a-z
        table = {}
        res = []

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in table:
                table[tuple(count)].append(word)
            else:
                table[tuple(count)] = [word]
        
        for key in table:
            res.append(table[key])
        
        return res

             




        