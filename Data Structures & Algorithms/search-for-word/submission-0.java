class Solution {
    private boolean search(char[][] board, String word, int r, int c, int i, boolean[][] visited) {
        if (i == word.length()) {
            return true;
        }

        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i) || visited[r][c] == true) {
            return false; 
        }

        visited[r][c] = true;
        boolean res = search(board, word, r + 1, c, i + 1, visited) || search(board, word, r, c + 1, i + 1, visited) || search(board, word, r - 1 , c, i + 1, visited) || search(board, word, r, c - 1, i + 1, visited);
        visited[r][c] = false;

        return res;
    }

    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (search(board, word, r, c, 0, visited) == true) {
                    return true;
                }
            }
        }
        return false;
    }
}
