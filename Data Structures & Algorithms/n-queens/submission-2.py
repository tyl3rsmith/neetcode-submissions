class Solution:
    def canPlace(self, board, r, c):
        # only need to check above this queen
        
        # checking vertically above for the presence of a queen in the same column
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        # checking above for the presence of a queen in the same diagonal 1
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # checking above for the presence of a queen in the same diagonal 2
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(r, board):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if self.canPlace(board, r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1, board)
                    board[r][c] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return res