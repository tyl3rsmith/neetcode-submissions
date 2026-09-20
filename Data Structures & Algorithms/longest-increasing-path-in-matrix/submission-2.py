class Solution:
    def dfs(self, r, c, prevValue, matrix, memo) -> int:
        if (r, c, prevValue) in memo:
            return memo[(r, c, prevValue)]

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # out of bounds
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return 0

        # not increasing
        if matrix[r][c] <= prevValue:
            return 0
        
        res = 1
        for dr, dc in directions:
            res = max(res, 1 + self.dfs(r + dr, c + dc, matrix[r][c], matrix, memo))
        
        memo[(r, c, prevValue)] = res
        return memo[(r, c, prevValue)]


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, self.dfs(r, c, float('-inf'), matrix, memo))
        
        return LIP

        
    