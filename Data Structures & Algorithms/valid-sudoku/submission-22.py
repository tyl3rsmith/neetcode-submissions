class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rowSet = {} # rows 0-9: set of elements we've seen
        colSet = {}
        squareSet = {}

        # initialize rows
        for r in range(ROWS):
            rowSet[r] = set()
        
        # initialize cols
        for c in range(COLS):
            colSet[c] = set()
        
        # initialize squares
        for r in range(3):
            for c in range(3):
                squareSet[(r, c)] = set()
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in rowSet[r] or
                    board[r][c] in colSet[c] or
                    board[r][c] in squareSet[(r//3, c//3)]):

                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[(r//3, c//3)].add(board[r][c])
        
        return True
