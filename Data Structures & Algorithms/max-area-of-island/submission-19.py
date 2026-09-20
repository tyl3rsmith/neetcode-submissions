class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # approach
        # every time we get a 1 run dfs on the island 
        # dfs returns area of island
        # keep track of the max result overall

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area


        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area