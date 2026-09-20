class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode as size,size,...,size#string
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            word_length = int(s[i : j])
            i = j + 1
            res.append(s[i : i + word_length])

            i = i + word_length
    
        return res

