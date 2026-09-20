class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        int r = 0, c = COLS - 1;

        while (c >= 0 && r < ROWS) {
            // staircase search, if too small move down
            if (matrix[r][c] < target) {
                r++;
            } else if (matrix[r][c] > target) { // if too large move left
                c--;
            } else {
                return true;
            }
        }
        return false;
    }
}
