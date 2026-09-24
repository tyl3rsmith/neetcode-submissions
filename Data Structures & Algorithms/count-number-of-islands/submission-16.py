class Solution:
    def explore(self, r: int, c: int, grid: List[List[str]]) -> None:
        grid[r][c] = "0"

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        for dr, dc in directions:
            if (r + dr < 0 or r + dr >= ROWS or c + dc < 0 or c + dc >= COLS) or (grid[r + dr][c + dc] == "0"):
                continue
            self.explore(r + dr, c + dc, grid)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    self.explore(r, c, grid)
        
        return islands


        