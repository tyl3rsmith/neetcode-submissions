class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def capture(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            for dr, dc in directions:
                capture(r + dr, c + dc)
        
        # 1. (BFS/DFS) Capture unsurrounded regions mark as (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if ((r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O'):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        # 3. Uncapture the unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
                