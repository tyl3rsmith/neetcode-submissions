class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        streak, curr = 0, nums[0]
        res = 0

        i = 0
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i] # new start point
                streak = 0 # reset streak
            while i < len(nums) and curr == nums[i]:
                i += 1 # move on, and skip duplicates
            
            curr += 1
            streak += 1
            res = max(res, streak)
        
        return res