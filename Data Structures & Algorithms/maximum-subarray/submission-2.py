class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force: try every subarray and compute the max
        res = float('-inf')
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                res = max(res, curr)
        
        return res


        