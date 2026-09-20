class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        
        res = 0

        def bfs_explore(r, c):
            q = deque([])
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    if (row + dr) in range(ROWS) and (col + dc) in range(COLS) and grid[row + dr][col + dc] != '0':
                        q.append((row + dr, col + dc))
                        grid[row + dr][col + dc] = '0'

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs_explore(r, c)
        
        return res
                
