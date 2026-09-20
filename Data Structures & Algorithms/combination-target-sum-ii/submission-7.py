class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr[:])
                return
            
            if currSum > target or i >= len(candidates):
                return
            
            # include candidates[i] at most once
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])
            curr.pop()

            # skip candidates[i] all together
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, currSum)
        
        dfs(0, [], 0)
        return res