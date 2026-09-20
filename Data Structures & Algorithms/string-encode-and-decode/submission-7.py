class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num, word = "", ""
            while s[i] != '#':
                num += s[i]
                i += 1

            i += 1
            end = i + int(num)
            while i < end:
                word += s[i]
                i += 1   
            res.append(word)
        
        return res
