class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                res = max(res, curr)
        
        return res

