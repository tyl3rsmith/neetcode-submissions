class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, prevValue):
            nonlocal pacific, atlantic

            if r < 0 or c < 0:
                pacific = True
                return
            
            if r >= ROWS or c >= COLS:
                atlantic = True
                return
             
            if heights[r][c] > prevValue or visited[r][c]:
                return
            
            visited[r][c] = True

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c])
                if pacific and atlantic:
                    break

            visited[r][c] = False
    
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])

        return res