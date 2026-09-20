class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach:
        # if the value is a 1 inc num islands run dfs on it and mark as 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                grid[row][col] = '0'

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0':
                        continue

                    q.append((nr, nc))

        numIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    numIslands += 1
                    bfs(r, c)
        
        return numIslands