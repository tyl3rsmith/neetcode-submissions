class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        # 2 3 4 4 5 10 20

        res, streak = 0, 0
        i, curr = 0, nums[0]

        while i < len(nums):
            if nums[i] != curr:
                streak = 0
                curr = nums[i]
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
    
        return res