class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force calculate the product of every thing except current position

        res = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        
        return res
        