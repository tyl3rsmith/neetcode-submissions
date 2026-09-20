class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1

        l, r = -1, -1
        resLen = float('inf')
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                if s[j] in countS:
                    countS[s[j]] += 1
                else:
                    countS[s[j]] = 1
                
                isSubstring = True
                for c in countT:
                    # c doesn't exist in s
                    if c not in countS:
                        isSubstring = False
                        break
                    
                    # not enough occurences
                    if countS[c] < countT[c]:
                        isSubstring = False
                        break
                
                if isSubstring and (j - i + 1) < resLen:
                    l, r = i, j
                    resLen = j - i + 1
                    break
        
        return s[l : r + 1] if resLen != float('inf') else ''


        
        