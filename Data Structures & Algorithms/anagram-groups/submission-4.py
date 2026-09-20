class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string count the frequencies of characters a-z
        table = {} # key: count -> val: list of words
        res = []

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            
            if key in table:
                table[key].append(word)
            else:
                table[key] = [word]
        

        for key in table:
            res.append(table[key])

        return res
            


                   

             




        