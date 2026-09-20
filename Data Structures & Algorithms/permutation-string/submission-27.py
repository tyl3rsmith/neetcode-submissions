class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force:
        # check every substring in s2
        # if s1 sorted == s2 sorted its true

        if len(s1) > len(s2):
            return False
        
        s1 = "".join(sorted(s1))
        
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                if len(s2[i : j + 1]) != len(s1):
                    continue
                
                print(s2[i : j + 1])

                if "".join(sorted(s2[i : j + 1])) == s1:
                    return True
                
        
        
        return False


