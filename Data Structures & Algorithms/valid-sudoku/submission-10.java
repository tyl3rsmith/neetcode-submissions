class Solution {
    public boolean isValidSudoku(char[][] board) {
        int numRows = board.length;
        int numCols = board[0].length;

        // check for duplicates across rows
        for (int r = 0; r < numRows; r++) {
            Set<Character> seen = new HashSet<>();
            for (int c = 0; c < numCols; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                if (seen.contains(board[r][c])) {
                    return false;
                }
                seen.add(board[r][c]);
            }
        }

        // check for duplicates across columns
        for (int c = 0; c < numCols; c++) {
            Set<Character> seen = new HashSet<>();
            for (int r = 0; r < numRows; r++) {
                if (board[r][c] == '.') {
                    continue;
                }
                if (seen.contains(board[r][c])) {
                    return false;
                }
                seen.add(board[r][c]);
            }
        }

        // check for duplicates across squares
        for (int square = 0; square < 9; square++) {
            Set<Character> seen = new HashSet<>();
            for (int r = 0; r < 3; r++) {
                for (int c = 0; c < 3; c++) {
                    int row = ((square / 3) * 3) + r;
                    int col = ((square % 3) * 3) + c;

                    if (board[row][col] == '.') {
                        continue;
                    }
                    if (seen.contains(board[row][col])) {
                        return false;
                    }
                    seen.add(board[row][col]);
                }
            }
        }

        return true;
        
    }
}
