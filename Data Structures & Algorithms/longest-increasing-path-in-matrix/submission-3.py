class Solution:
    def dfs(self, r, c, prevValue, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # out of bounds
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return 0

        # not increasing
        if matrix[r][c] <= prevValue:
            return 0
        
        LIP = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            LIP = max(LIP, 1 + self.dfs(r + dr, c + dc, matrix[r][c], matrix))
        
        return LIP

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, self.dfs(r, c, float('-inf'), matrix))
        
        return LIP


        
    