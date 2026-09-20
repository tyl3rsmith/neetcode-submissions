class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach:
        # if the value is a 1 inc num islands run dfs on it and mark as 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        numIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfs(r, c)
        
        return numIslands