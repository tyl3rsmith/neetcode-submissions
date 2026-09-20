class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        
        first = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[-1] = first


        return self.findMin(nums)
        