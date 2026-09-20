class Solution {
    public boolean isValidSudoku(char[][] board) {
        // key: row/col/square, value: set of chars present there
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<List<Integer>, Set<Character>> squares = new HashMap<>();

        int numRows = 9, numCols = 9;
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                List<Integer> squareKey = Arrays.asList(r/3, c/3);

                // check duplicates
                if (rows.containsKey(r)) {
                    if (rows.get(r).contains(board[r][c])) {
                        return false;
                    }   
                } else {
                    rows.put(r, new HashSet<>());
                }
                rows.get(r).add(board[r][c]);


                if (cols.containsKey(c)) {
                    if (cols.get(c).contains(board[r][c])) {
                        return false;
                    }   
                } else {
                    cols.put(c, new HashSet<>());
                }
                cols.get(c).add(board[r][c]);


                if (squares.containsKey(squareKey)) {
                    if (squares.get(squareKey).contains(board[r][c])) {
                        return false;
                    }   
                } else {
                    squares.put(squareKey, new HashSet<>());
                }
                squares.get(squareKey).add(board[r][c]);
            }
        }
        return true;
    }
}
