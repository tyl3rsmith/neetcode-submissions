class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, soln = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(soln[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            # include the number
            soln.append(candidates[i])

            # backtrack, increase total and we cant reuse the number
            backtrack(i + 1, total + candidates[i])

            # cleanup
            soln.pop()

            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res