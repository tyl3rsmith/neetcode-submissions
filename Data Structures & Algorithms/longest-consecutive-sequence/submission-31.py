class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start from every spot and find the lcs

        res = 0
        num_set = set(nums)

        for num in nums:
            current_streak = 0
            current = num

            while current in num_set:
                current += 1
                current_streak += 1
            
            res = max(res, current_streak)
            
        return res
        