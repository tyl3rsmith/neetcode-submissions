class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak = 0
            curr = num

            while curr in store:
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

    [2, 20, 4, 10, 3, 4, 5]
    {2, 30, 4, 10, 3, 4, 5}
"""