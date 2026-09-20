class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c):
            visited = [[False] * COLS for _ in range(ROWS)]
            q = deque([(r, c)])
            visited[r][c] = True

            dist = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return dist
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or visited[nr][nc] or grid[nr][nc] == -1:
                            continue

                        q.append((nr, nc))
                        visited[nr][nc] = True
                    
                dist += 1

            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
        