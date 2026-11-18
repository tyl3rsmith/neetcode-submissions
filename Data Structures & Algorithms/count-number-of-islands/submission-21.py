class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        islands = 0

        def bfs(r, c):
            if grid[r][c] == "0": # already explored island
                return
            
            grid[r][c] = "0" # mark island as explored

            queue = deque() # start exploring from the source
            queue.append((r, c))

            while queue: # keep exploring while we have valid positions in the queue
                r, c = queue.popleft() # currrent position being considered
                for dr, dc in directions: # visit all unexplored neighbors
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1": # make sure they're in bounds
                        queue.append((nr, nc)) # add to queue to be processed
                        grid[nr][nc] = "0" # mark as visited before next iteration of the loop

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands