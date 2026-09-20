class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([])
            q.append((r, c))
            visited.add((r, c))

            curr_area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    if ((row + dr) in range(ROWS) and
                        (col + dc) in range(COLS) and
                        (row + dr, col + dc) not in visited and
                        grid[row + dr][col + dc] == 1):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
                        curr_area += 1
            
            return curr_area
            

        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
