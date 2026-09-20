class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        sizes = []
        res = ""

        for word in strs:
            sizes.append(len(word))
        
        for sz in sizes:
            res += str(sz) + ','
        
        res += '#'
        for word in strs:
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        print(s)

        sizes = []
        res = []
        i = 0

        while s[i] != '#':
            curr_size = ''
            while s[i] != ',':
                curr_size += s[i]
                i += 1
            sizes.append(int(curr_size))
            i += 1
        i += 1

        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz

        return res

            
        