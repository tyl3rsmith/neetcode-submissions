class Solution:
    def backtrack(self, board, r, n, cols, posDiag, negDiag, res):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or r + c in posDiag or r - c in negDiag:
                continue

            board[r][c] = "Q"
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)

            self.backtrack(board, r + 1, n, cols, posDiag, negDiag, res)

            board[r][c] = "."
            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()
        self.backtrack(board, 0, n, cols, posDiag, negDiag, res)
        return res