class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        print(candidates)

        def dfs(combination, currSum, i):
            if (currSum == target):
                res.append(combination[:])
                return
            if (i == n):
                return

            # include candidates[i] as long as candidates[i] + currSum <= target
            if (candidates[i] + currSum <= target):
                combination.append(candidates[i])
                dfs(combination, candidates[i] + currSum, i + 1)
                combination.pop() # backtrack
            
            
            # dont include candidates[i] in combination and skip duplicates
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(combination, currSum, i + 1)

        dfs([], 0, 0)
        return res
        