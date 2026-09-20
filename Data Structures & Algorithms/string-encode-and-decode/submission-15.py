class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding += str(len(word)) + '#' + word
        return encoding

    def decode(self, s: str) -> List[str]:
        print(s)
        decoding = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            print(length)
            i = j + 1
            j = i + length
            print(i, j)

            decoding.append(s[i:j])
            i = j


        return decoding