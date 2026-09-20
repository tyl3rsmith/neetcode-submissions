class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        return res where res[i] is the product of all the elements of nums except nums[i]
        """
        res = [0] * len(nums)

        for i in range(len(nums)):
            nums_product = 1
            for j in range(len(nums)):
                if i != j:
                    nums_product *= nums[j]
                    res[i] = nums_product
        return res


        