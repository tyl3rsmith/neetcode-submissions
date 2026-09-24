class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        islands = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    queue.append((r, c))

                    while queue:
                        row, col = queue.popleft()
                        grid[row][col] = "0"

                        for dr, dc in directions:
                            if (row + dr < 0 or row + dr >= ROWS or
                                col + dc < 0 or col + dc >= COLS or
                                grid[row + dr][col + dc] == "0"):
                                continue

                            queue.append((row + dr, col + dc))
                            grid[row + dr][col + dc] = "0"
                        
                        # print(queue)
                    
        
        return islands


        