class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            leftProduct = 1
            for j in range(i - 1, -1, -1):
                leftProduct *= nums[j]

            rightProduct = 1
            for j in range(i + 1, n):
                rightProduct *= nums[j]

            res[i] = leftProduct * rightProduct
        
        return res

