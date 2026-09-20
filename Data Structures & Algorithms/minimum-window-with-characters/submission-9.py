class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        countT = {}
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
            
        res = [-1, -1]
        resLen = float("infinity")

        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                if s[j] in countS:
                    countS[s[j]] += 1
                else:
                    countS[s[j]] = 1
                
                flag = True
                # check if this substring doesnt contain t
                for c in countT:
                    if (c in countS and countT[c] > countS[c]) or (c not in countS and countT[c] > 0):
                        flag = False
                        break
                
                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""                


        
        return res
                