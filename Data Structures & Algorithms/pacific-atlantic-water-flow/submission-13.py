class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        pac = set()
        atl = set()
        
        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            if (r, c) in visit:
                return

            if heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

    

        for r in range(ROWS):
            dfs(r, 0, pac, float('-inf'))
            dfs(r, COLS - 1, atl, float('-inf'))
        
        for c in range(COLS):
            dfs(0, c, pac, float('-inf'))
            dfs(ROWS - 1, c, atl, float('-inf'))
        
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        
        return res

