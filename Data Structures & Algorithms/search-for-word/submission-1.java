class Solution {
    private boolean search(char[][] board, String word, int i, int r, int c, boolean[][] visited) {
        if (i == word.length()) {
            return true;
        }

        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || visited[r][c] || word.charAt(i) != board[r][c]) {
            return false;
        }

        visited[r][c] = true;
        boolean res =
            search(board, word, i + 1, r + 1, c, visited) ||
            search(board, word, i + 1, r - 1, c, visited) ||
            search(board, word, i + 1, r, c + 1, visited) ||
            search(board, word, i + 1, r, c - 1, visited);

        visited[r][c] = false;
        return res;

    }

    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (search(board, word, 0, r, c, visited)) {
                    return true;
                }
            }
        }

        return false;
    }
}
