class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            temp_res = 1
            curr = num + 1
            while curr in num_set:
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