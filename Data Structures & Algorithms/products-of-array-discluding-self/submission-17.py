class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        print(res)

        # brute force approach
        # compute left and right product for each position in the array

        for i in range(len(nums)):

            left_product = 1
            for j in range(0, i):
                left_product *= nums[j]
            
            right_product = 1
            for j in range(i + 1, len(nums)):
                right_product *= nums[j]
            
            res[i] = left_product * right_product
            
        return res
        