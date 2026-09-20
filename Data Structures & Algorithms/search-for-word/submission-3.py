class Solution:
    def dfs(self, board, word, i, r, c, visited):
        if i == len(word):
            return True
        
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i] or visited[r][c]:
            return False
        
        visited[r][c] = True
        res = (
            self.dfs(board, word, i + 1, r + 1, c, visited) or
            self.dfs(board, word, i + 1, r - 1, c, visited) or
            self.dfs(board, word, i + 1, r, c + 1, visited) or
            self.dfs(board, word, i + 1, r, c - 1, visited)
        )
        visited[r][c] = False
        return res



    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        for r in range(ROWS):
            for c in range(COLS):
                if self.dfs(board, word, 0, r, c, visited):
                    return True
        
        return False
        