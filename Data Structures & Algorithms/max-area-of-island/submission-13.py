class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([])
            q.append((r, c))
            visited.add((r, c))

            curr_area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc   

                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        curr_area += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
                
            return curr_area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
