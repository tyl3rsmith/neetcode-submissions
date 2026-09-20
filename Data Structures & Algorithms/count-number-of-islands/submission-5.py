class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_explore(r, c):
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dy, dx in directions:
                if (r + dx) in range(ROWS) and (c + dy) in range(COLS):
                    dfs_explore(r + dx, c + dy)


        ROWS, COLS = len(grid), len(grid[0])
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    dfs_explore(r, c)
        
        return res
                
