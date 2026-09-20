class Solution {
    private boolean dfs(char[][] board, String word, int r, int c, int i, Set<String> path) {
        if (i == word.length()) {
            return true;
        }

        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || word.charAt(i) != board[r][c] || path.contains(r + "," + c)) {
            return false;
        }

        path.add(r + "," + c);

        boolean res =
            dfs(board, word, r + 1, c, i + 1, path) ||
            dfs(board, word, r - 1, c, i + 1, path) ||
            dfs(board, word, r, c + 1, i + 1, path) ||
            dfs(board, word, r, c - 1, i + 1, path);

        path.remove(r + "," + c);
        return res;
    }


    public boolean exist(char[][] board, String word) {
        int ROWS = board.length;
        int COLS = board[0].length;
        Set<String> path = new HashSet<>();

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (dfs(board, word, r, c, 0, path)) {
                    return true;
                }
            }
        }
        return false;
    }
}
