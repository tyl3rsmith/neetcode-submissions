class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix products

        res = [0] * len(nums)
        
        leftProduct = [1] * len(nums)
        for l in range(1, len(nums)):
            leftProduct[l] = leftProduct[l - 1] * nums[l - 1]
        
        rightProduct = [1] * len(nums)
        for r in range(len(nums) - 2, -1, -1):
            rightProduct[r] = rightProduct[r + 1] * nums[r + 1]
        
        for i in range(len(res)):
            res[i] = leftProduct[i] * rightProduct[i]

        return res