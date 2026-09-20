class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dfs(i):
            if i == 0:
                return nums[0]
            
            prev = dfs(i - 1)
            return max(nums[i], nums[i] + prev)
        
        # Compute f(i) for all indices and return the max
        best = float('-inf')
        for i in range(n):
            best = max(best, dfs(i))
        return best
