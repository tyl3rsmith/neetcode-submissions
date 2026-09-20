class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
            

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        
        return area
        