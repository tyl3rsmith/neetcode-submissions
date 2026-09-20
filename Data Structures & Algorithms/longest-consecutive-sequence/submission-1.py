class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res = []
        num_set = set(nums)
        for num in nums:
            if ((num - 1) not in num_set): # this is the start of a sequence
                next_elem = num + 1
                temp_res = []
                while next_elem in num_set:
                    temp_res.append(next_elem)
                    next_elem += 1
                if (len(temp_res) > len(res)):
                    res = temp_res
        return len(res) + 1




"""
    nums: list[int]
    return longest consecutive sequence
    each element is exactly 1 greater than the previous element
    elements do not have to be consecutive in the original array
    O(n) time

    [2, 20, 4, 10, 3, 4, 5]
    {2, 30, 4, 10, 3, 4, 5}
"""