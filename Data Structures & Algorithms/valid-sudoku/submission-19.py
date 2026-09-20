class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # validate each row
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        # validate each column
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        
        # validate each square
        for square in range(9):
            seen = set()

            for i in range(3): # row offset
                for j in range(3): # col offset
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == '.':
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True