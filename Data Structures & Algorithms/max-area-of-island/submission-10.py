class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            grid[r][c] = 0
            curr_area = 1

            for dr, dc in directions:
                if ((r + dr) in range(ROWS) and
                    (c + dc) in range(COLS) and
                    grid[r + dr][c + dc] == 1):
                    curr_area += dfs(r + dr, c + dc)
            
            return curr_area


        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area

        