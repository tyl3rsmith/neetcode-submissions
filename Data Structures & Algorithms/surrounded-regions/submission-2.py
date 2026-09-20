class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def bfs():
            q = deque()

            for r in range(ROWS):
                for c in range(COLS):
                    if (board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                        q.append((r, c))
            
            while q:
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'T'

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if nr in range(ROWS) and nc in range(COLS):
                            q.append((nr, nc))
            
        
        # 1. (BFS) Capture unsurrounded regions mark as (O -> T)
        bfs()


        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                # 3. Uncapture the unsurrounded regions (T -> O)
                if board[r][c] == 'T':
                    board[r][c] = 'O'
