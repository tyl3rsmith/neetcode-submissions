class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, sum(nums[i:j+1]))
        
        return res