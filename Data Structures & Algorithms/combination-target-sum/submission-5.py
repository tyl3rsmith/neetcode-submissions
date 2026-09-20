class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr[:])
                return
            
            if i >= len(nums) or currSum > target:
                return
            
            # include nums[i] 1 or more times
            curr.append(nums[i])
            dfs(i, curr, currSum + nums[i])
            curr.pop()

            # skip nums[i] all together
            dfs(i + 1, curr, currSum)
        
        dfs(0, [], 0)
        return res
