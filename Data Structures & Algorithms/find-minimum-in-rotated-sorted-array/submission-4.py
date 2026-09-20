class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        new = [0] * len(nums)
        new[0] = nums[-1]
        for i in range(1, len(nums)):
            new[i] = nums[i - 1]

        return self.findMin(new)
        