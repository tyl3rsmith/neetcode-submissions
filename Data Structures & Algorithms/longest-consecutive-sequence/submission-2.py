class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if ((num - 1) not in num_set): # start of sequence
                temp_res = 1
                while (num + temp_res) in num_set:
                    temp_res += 1
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