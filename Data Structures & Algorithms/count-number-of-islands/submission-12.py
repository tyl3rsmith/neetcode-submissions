class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if row + dr in range(ROWS) and col + dc in range(COLS) and grid[row + dr][col + dc] == '1':
                        grid[row + dr][col + dc] = '0'
                        q.append((row + dr, col + dc))
            return
    
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands