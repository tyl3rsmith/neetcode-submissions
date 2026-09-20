class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        int r = ROWS - 1, c = 0;

        while (c < COLS && r >= 0) {
            // staircase search, if too small move to the right
            if (matrix[r][c] < target) {
                c++;
            } else if (matrix[r][c] > target) { // if too large move up
                r--;
            } else {
                return true;
            }
        }
        return false;
    }
}
