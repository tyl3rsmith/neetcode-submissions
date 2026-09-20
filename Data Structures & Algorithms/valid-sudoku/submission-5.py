class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} # key -> row, val -> set of nums in the row
        cols = {} # key -> col, val -> set of nums in the col
        squares = {} # key -> (r//3, c//3), val -> set of nums in the square

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue

                if r not in rows:
                    rows[r] = set()
                
                if c not in cols:
                    cols[c] = set()
                
                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = set()

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
                