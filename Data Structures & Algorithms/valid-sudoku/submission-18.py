class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            rows = set()
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in rows:
                    return False
                else:
                    rows.add(board[r][c])
        
        for c in range(COLS):
            cols = set()
            for r in range(ROWS):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in cols:
                    return False
                else:
                    cols.add(board[r][c])
        
        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == '.':
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True

        
