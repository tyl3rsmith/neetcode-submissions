class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix products

        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res

        