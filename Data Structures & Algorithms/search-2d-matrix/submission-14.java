class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        for (int r = 0; r < ROWS; r++) {
            // target falls in this row
            if (target >= matrix[r][0] && target <= matrix[r][COLS - 1]) {
                for (int c = 0; c < COLS; c++) {
                    if (matrix[r][c] == target) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
