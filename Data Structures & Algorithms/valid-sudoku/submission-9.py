class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if c not in cols: # first time visiting this column
                    cols[c] = set()
                if r not in rows:
                    rows[r] = set()
                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = set()
                
                if (board[r][c] in cols[c] or # check for duplicates
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c]) # update sets
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
                    