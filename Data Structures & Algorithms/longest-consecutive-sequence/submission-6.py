class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: # if nums is empty we return 0
            return 0

        nums.sort() # sort nums in ascending order

        res = 0
        streak = 0

        i = 0
        curr = nums[0]

        while i < len(nums):
            if (nums[i] != curr): # start of another sequence
                streak = 0
                curr = nums[i]
            
            while (i < len(nums) and nums[i] == curr): # skip over duplicate entries
                i += 1
            
            streak += 1
            curr += 1
            
            res = max(res, streak)
            
        return res




"""
    nums: list[int]
    return longest consecutive sequence
    each element is exactly 1 greater than the previous element
    elements do not have to be consecutive in the original array
    O(n) time
    [2, 3, 4, 4, 5, 10, 20]
"""