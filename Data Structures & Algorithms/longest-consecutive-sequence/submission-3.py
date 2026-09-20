class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()
        res = 0
        temp_res = 0
        curr = nums[0]

        i = 0
        while i < len(nums):
            if curr != nums[i]:
                temp_res = 0
                curr = nums[i]
            while i < len(nums) and nums[i] == curr:
                i += 1
            temp_res += 1
            curr += 1
            res = max(res, temp_res)
    
        return res




"""
    nums: list[int]
    return longest consecutive sequence
    each element is exactly 1 greater than the previous element
    elements do not have to be consecutive in the original array
    O(n) time

    [2, 20, 4, 10, 3, 4, 5]
    {2, 30, 4, 10, 3, 4, 5}
"""