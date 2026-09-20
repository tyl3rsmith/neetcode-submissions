class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force scan every row/col/sub grid for duplicates
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[c][r] == '.':
                    continue
                if board[c][r] in seen:
                    return False
                seen.add(board[c][r])
        
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c

                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
                     



                    




        