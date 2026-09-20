class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(permutation, used):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    permutation.append(nums[i])
                    used[i] = True
                    dfs(permutation, used)
                    used[i] = False
                    permutation.pop()
        
        dfs([], [False] * len(nums))
        return res
            

