class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS: prev index is j, current index i
        n = len(nums)
        memo = [-1] * n

        # LIS starting with num[i]
        def dfs(i):
            # base case: no digit to process, len of LIS is 0
            if i == n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            # if we're here we have at least one digit
            LIS = 1
            for j in range(i + 1, n):
                # expand the sequence only if the next number is larger
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))
                    
            memo[i] = LIS
            return LIS
        
        res = -1
        for i in range(n):
            res = max(res, dfs(i))
        
        return res
