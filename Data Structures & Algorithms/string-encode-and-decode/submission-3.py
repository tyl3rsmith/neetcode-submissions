class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # j goes until and stops at #
                j += 1
            length = int(s[i:j]) # length of the word
            i = j + 1 # i becomes the first character after #
            j = i + length # j goes to the start of the next num
            res.append(s[i:j])
            i = j

        return res  