class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(combination, currSum, i):
            if (currSum == target):
                res.append(combination[:])
                return
            if (i == n):
                return
            
            # keep adding nums[i] while we haven't exceeded the target
            if currSum + nums[i] <= target:
                combination.append(nums[i])
                dfs(combination, currSum + nums[i], i)
                combination.pop()
            
            # we can always choose to skip nums[i] and move on to nums[i + 1]
            dfs(combination, currSum, i + 1)

        dfs([], 0, 0)
        return res
        

