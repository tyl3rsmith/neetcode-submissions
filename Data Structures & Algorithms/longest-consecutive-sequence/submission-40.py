class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = nums

        res = 0
        for num in numSet:
            length = 1

            while num + length in numSet:
                length += 1

            res = max(res, length)

        return res