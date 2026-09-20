class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        streak = 1
        res = 0

        for num in nums:
            if (num - 1) not in num_set: # this is a candidate for a max sequence
                next_elem = num + 1
                while (next_elem) in num_set:
                    streak += 1
                    next_elem += 1
                res = max(res, streak)
                streak = 1 # reset streak for next iteration
        
        return res






"""
    nums: list[int]
    return longest consecutive sequence
    each element is exactly 1 greater than the previous element
    elements do not have to be consecutive in the original array
    O(n) time
    [2, 3, 4, 4, 5, 10, 20]
"""