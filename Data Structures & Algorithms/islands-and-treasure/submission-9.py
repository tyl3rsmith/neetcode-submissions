class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            visited = [[False] * COLS for _ in range(ROWS)]
            q = deque([])
            q.append((r, c))
            visited[r][c] = True
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            steps = 0

            while q:
                # process level by level
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if not (nr in range(ROWS) and nc in range(COLS) and not visited[nr][nc] and grid[nr][nc] != -1):
                            continue
                        
                        q.append((nr, nc))
                        visited[nr][nc] = True

                # after done with current level we inc steps
                steps += 1
            
            # we never got to a treasure chest
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
        