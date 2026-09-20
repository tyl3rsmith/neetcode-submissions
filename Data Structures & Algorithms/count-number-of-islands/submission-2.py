class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # down, up, right, left
            grid[r][c] = '0'
            queue = deque([(r, c)])

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if (new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols or grid[new_row][new_col] != '1'):
                        continue
                    else:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = '0'
            return
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r, c)
        
        return num_islands



        