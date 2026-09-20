class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            grid[r][c] = '0'
            queue = deque([(r, c)])

            while queue:
                row, col = queue.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]] # up, down, right, left

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == '1'):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands
        

        






        