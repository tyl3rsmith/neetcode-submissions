class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if not (r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1):
                return 0
            
            visited.add((r, c))
            area = 1

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area