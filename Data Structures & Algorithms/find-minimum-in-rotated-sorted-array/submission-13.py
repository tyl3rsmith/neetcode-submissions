class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # we are in a fully sorted portion
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # binary search, middle could be a solution
            m = l + (r - l) // 2
            res = min(res, nums[m])

            # we are in the left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else: # right sorted portion min is in here
                r = m - 1
        
        return res
