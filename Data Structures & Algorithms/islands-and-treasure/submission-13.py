class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        INF = 2147483647

        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == -1:
                        continue

                    q.append((nr, nc))          
                    visit.add((nr, nc))  
            level += 1





        