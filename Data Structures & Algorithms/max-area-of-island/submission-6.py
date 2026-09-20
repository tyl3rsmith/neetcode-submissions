class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 1

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                        area += 1
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        return max_area