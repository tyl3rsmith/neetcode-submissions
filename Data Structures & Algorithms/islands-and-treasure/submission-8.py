class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = deque()
            visited = [[False] * COLS for _ in range(ROWS)]
            q.append((r, c))
            visited[r][c] = True
            dist = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return dist

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1 or visited[nr][nc]:
                            continue

                        visited[nr][nc] = True
                        q.append((nr, nc))

                dist += 1
                
            return INF
                    


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        

        
        