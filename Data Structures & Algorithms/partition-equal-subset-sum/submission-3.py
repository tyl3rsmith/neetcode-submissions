class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)

        if n % 2:
            return False

        target = n // 2
        used = [False] * n
        
        def dfs(target):
            if target == 0:
                return True
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    if dfs(target - nums[i]):
                        return True
                    used[i] = False

            return False

        return dfs(target)  