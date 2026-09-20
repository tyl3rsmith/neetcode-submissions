class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # approach
        # every time we get a 1 run dfs on the island 
        # dfs returns area of island
        # keep track of the max result overall

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        
        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 0

            while q:
                row, col = q.popleft()
                area += 1
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 0
                    q.append((nr, nc))
            
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area