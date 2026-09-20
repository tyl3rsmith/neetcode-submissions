class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            if c in count1:
                count1[c] += 1
            else:
                count1[c] = 1
        
        need = len(count1)

        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                if s2[j] in count2:
                    count2[s2[j]] += 1
                else:
                    count2[s2[j]] = 1
                
                # not a char in s2 or occurs too many times in s2
                if s2[j] not in count1 or s2[j] in count1 and count2[s2[j]] > count1[s2[j]]:
                    break

                # exact match
                if s2[j] in count1 and count1[s2[j]] == count2[s2[j]]:
                    cur += 1 # number of exact matches increases
                
                if cur == need:
                    return True
        return False