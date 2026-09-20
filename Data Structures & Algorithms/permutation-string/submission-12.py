class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = {}
        for i in range(len(s1)):
            if s1[i] in s1_counts:
                s1_counts[s1[i]] += 1
            else:
                s1_counts[s1[i]] = 1

        s2_counts = {}
        for i in range(len(s1)):
            if s2[i] in s2_counts:
                s2_counts[s2[i]] += 1
            else:
                s2_counts[s2[i]] = 1
        
        if s1_counts == s2_counts:
            return True

        #print(s1_counts)

        l = 0
        for r in range(len(s1), len(s2)):
            #print(s2_counts)
            s2_counts[s2[l]] -= 1

            if s2_counts[s2[l]] == 0:
                del s2_counts[s2[l]]

            if s2[r] in s2_counts:
                s2_counts[s2[r]] += 1
            else:
                s2_counts[s2[r]] = 1

            l += 1

            if s1_counts == s2_counts:
                return True
        
        return False
            

