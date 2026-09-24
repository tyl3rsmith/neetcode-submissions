class Solution:
    def countArea(self, r: int, c: int, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        area = 1
        grid[r][c] = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or not grid[nr][nc]):
                continue

            area += self.countArea(nr, nc, grid)

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    maxArea = max(maxArea, self.countArea(r, c, grid))
        
        return maxArea