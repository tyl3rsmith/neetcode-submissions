class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l < r:
            m = l + (r - l) // 2
            # minimum is in the right half
            if nums[m] < nums[r]:
                r = m
            # minimum is in the left half
            else:
                l = m + 1
        
        return nums[r]