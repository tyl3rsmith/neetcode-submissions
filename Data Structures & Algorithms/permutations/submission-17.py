class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        picked = [False] * n
        res = []

        def dfs(curr, i, picked):
            if (len(curr) == n):
                res.append(curr[:])
                return
            
            for i in range(n):
                # include any of nums[i] if it's not already picked
                if (not picked[i]):
                    curr.append(nums[i])
                    picked[i] = True
                    dfs(curr, i + 1, picked)
                    curr.pop()
                    picked[i] = False
                
        
        dfs([], 0, picked)
        return res
