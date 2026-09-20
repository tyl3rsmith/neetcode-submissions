class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # starting queues for bfs
        pacific = []
        atlantic = []

        pac = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atl = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # initial positions that can reach atlantic/pacific ocean
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        def bfs(source, ocean):
            q = deque(source)

            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(ROWS) and nc in range(COLS) and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))
            
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append((r, c))
        
        return res