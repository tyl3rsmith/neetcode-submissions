class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        
        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            i = j
            num = ''
            if j < len(s):
                while s[j] != '#':
                    num += s[j]
                    j += 1
                length = int(num)
                i = j + 1
                j = i + length
                res.append(s[i:j]) 

        return res
                



            
        