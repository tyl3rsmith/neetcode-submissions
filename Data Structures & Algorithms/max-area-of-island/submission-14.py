class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0

            visited.add((r, c))

            curr_area = 1
            for dr, dc in directions:
                curr_area += dfs(r + dr, c + dc)
            
            return curr_area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
