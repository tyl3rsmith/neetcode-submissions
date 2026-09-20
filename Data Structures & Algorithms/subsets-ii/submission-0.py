class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return

            # include
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            # skip over duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # dont include
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res