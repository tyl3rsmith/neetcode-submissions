class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            if grid[r][c] == 0:
                return 0
                
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1
            
            return area
                    
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, bfs(r, c))
        
        return area