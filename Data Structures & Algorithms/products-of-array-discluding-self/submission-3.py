class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)
        res = [0] * len(nums)

        prefix_products[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_products[i] *= prefix_products[i - 1] * nums[i]

        suffix_products[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i]


        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix_products[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix_products[i - 1]
            else:
                res[i] = prefix_products[i - 1] * suffix_products[i + 1]
        
        return res


        