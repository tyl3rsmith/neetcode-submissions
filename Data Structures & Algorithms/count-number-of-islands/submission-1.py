class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def dfs(r, c):
            if (r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] != '1'):
                return
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # down, up, right, left
            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands



        