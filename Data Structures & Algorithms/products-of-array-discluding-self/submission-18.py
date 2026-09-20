class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] * len(nums)

        for i in range(1, len(nums)):
            leftProducts[i] = nums[i - 1] * leftProducts[i - 1]
        
        print(leftProducts)

        rightProducts = [1] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = nums[i + 1] * rightProducts[i + 1]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = leftProducts[i] * rightProducts[i]
        
        return res

        
