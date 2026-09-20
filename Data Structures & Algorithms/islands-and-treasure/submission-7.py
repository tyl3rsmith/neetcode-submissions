class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        

        def bfs(r, c):
            q = deque([(r, c)])
            visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
            visited[r][c] = True
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr in range(ROWS) and
                            nc in range(COLS) and
                            not visited[nr][nc] and
                            grid[nr][nc] != -1):
                            q.append((nr, nc))
                            visited[nr][nc] = True
                steps += 1
            return steps
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        