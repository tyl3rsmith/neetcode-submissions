class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode as size,size,...,size#string
        res = ""
        for word in strs:
            res += str(len(word))
            res += ','
        
        res += '#'
        res += ''.join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        sizes = []

        i = 0
        while i < len(s) and s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            
            sizes.append(int(s[i:j]))
            i = j + 1
        
        i += 1
        res = []
        for size in sizes:
            res.append(s[i:i+size])
            i += size

        return res
