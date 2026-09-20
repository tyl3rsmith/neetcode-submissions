class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([])
            q.append((r, c, 0))
            seen = set()

            while q:
                row, col, dist = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and 
                        grid[nr][nc] not in [0, -1] and
                        (nr, nc) not in seen):
                        grid[nr][nc] = min(dist + 1, grid[nr][nc])
                        q.append((nr, nc, dist + 1))
                        seen.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)
        