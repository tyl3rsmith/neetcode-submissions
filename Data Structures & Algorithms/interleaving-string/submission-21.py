class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [False for _ in range(m + 1)]
        dp[m] = True

        for j in range(m - 1, -1, -1):
            dp[j] = s2[j] == s3[n + j] and dp[j + 1]
        
        for i in range(n - 1, -1, -1):
            new_dp =  [False for _ in range(m + 1)]
            new_dp[m] = s1[i] == s3[i + m] and dp[m]

            for j in range(m - 1, -1, -1):
                if s1[i] == s3[i + j]:
                    if dp[j]:
                        new_dp[j] = dp[j]
                
                if s2[j] == s3[i + j]:
                    if new_dp[j + 1]:
                        new_dp[j] = new_dp[j + 1]

            dp = new_dp
        
        return dp[0]
        
