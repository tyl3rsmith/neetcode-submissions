class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([])
            q.append((r, c, 0))
            seen = set()

            while q:
                row, col, dist = q.popleft()
                
                for dr, dc in directions:
                    if ((row + dr) in range(ROWS) and
                        (col + dc) in range(COLS) and 
                        grid[row + dr][col + dc] != 0 and
                        grid[row + dr][col + dc] != -1 and
                        (row + dr, col + dc) not in seen):
                        grid[row + dr][col + dc] = min(dist + 1, grid[row + dr][col + dc])
                        q.append((row + dr, col + dc, dist + 1))
                        seen.add((row + dr, col + dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)
            
        