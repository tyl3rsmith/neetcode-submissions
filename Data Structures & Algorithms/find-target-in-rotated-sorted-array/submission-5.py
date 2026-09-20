class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m

            # we are in the left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                elif target < nums[m] and target >= nums[l]:
                    r = m - 1

            # we are in the right sorted portion
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                elif target <= nums[r] and target > nums[m]:
                    l = m + 1
        
        return -1
                