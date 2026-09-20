class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            grid[r][c] = 0
            area = 1
            queue = deque([(r, c)])

            while queue:
                row, col = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == 1):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 0
                        area += 1
                        
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        
        return max_area
