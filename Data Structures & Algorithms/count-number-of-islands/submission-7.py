class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            visited.add((r, c))
            q = deque([])
            q.append((r, c))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    if ((row + dr) in range(ROWS) and
                        (col + dc) in range(COLS) and
                        grid[row + dr][col + dc] == '1' and
                        (row + dr, col + dc) not in visited):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands