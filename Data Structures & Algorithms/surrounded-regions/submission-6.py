class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def capture():
            q = deque()

            for r in range(ROWS):
                for c in range(COLS):
                    if (board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                        q.append((r, c))
            
            while q:
                r, c = q.popleft()
                board[r][c] = 'T'

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == 'O':
                        q.append((nr, nc))
        
        capture()
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                