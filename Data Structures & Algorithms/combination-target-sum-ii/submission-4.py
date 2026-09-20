class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, sol, total):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            # include in sum
            sol.append(candidates[i])
            dfs(i + 1, sol, total + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # dont include
            dfs(i + 1, sol, total)

        dfs(0, [], 0)
        return res