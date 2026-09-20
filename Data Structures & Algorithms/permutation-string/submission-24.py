class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if count1[i] == count2[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # add char to window
            count2[ord(s2[r]) - ord('a')] += 1
            if count1[ord(s2[r]) - ord('a')] == count2[ord(s2[r]) - ord('a')]: # equal counts
                matches += 1
            elif count1[ord(s2[r]) - ord('a')] + 1 == count2[ord(s2[r]) - ord('a')]: # overshot by 1
                matches -= 1

            # remove char from window
            count2[ord(s2[l]) - ord('a')] -= 1
            if count1[ord(s2[l]) - ord('a')] == count2[ord(s2[l]) - ord('a')]: # equal counts
                matches += 1
            elif count1[ord(s2[l]) - ord('a')] - 1 == count2[ord(s2[l]) - ord('a')]: # were equal but now they aren't
                matches -= 1
            
            l += 1
        return matches == 26