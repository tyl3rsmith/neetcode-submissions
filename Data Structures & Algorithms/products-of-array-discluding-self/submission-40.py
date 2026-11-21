class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prod = 1
        for i in range(1, len(nums)):
            res[i] = prod * nums[i - 1]
            prod *= nums[i - 1]

        suff = 1
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suff * nums[i + 1]
            suff *= nums[i + 1]
        
        return res