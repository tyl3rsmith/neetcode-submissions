class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, soln = [], []

        def backtrack(i, total):
            if total == target:
                res.append(soln[:])
                return
            
            if i == len(nums) or total > target:
                return
            
            # include this value
            soln.append(nums[i])
            backtrack(i, total + nums[i])
            soln.pop()

            # skip this value in the other branches
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res
        