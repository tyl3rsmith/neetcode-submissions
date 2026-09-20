class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;
        
        int l = 0, r = ROWS - 1;
        int rowIdx = -1;
        while (l <= r) {
            int m = l + ((r - l) / 2);
            // check the rows above
            if (target < matrix[m][0]) {
                r = m - 1;
            // check the rows below
            } else if (target > matrix[m][COLS - 1]) {
                l = m + 1;
            } else {
                // target lies within this row
                rowIdx = m;
                break;
            }
        }
        if (rowIdx == -1) {
            return false;
        }

        // binary search the row to see if the target exists
        l = 0; r = COLS - 1;
        while (l <= r) {
            int m = l + ((r - l) / 2);
            if (matrix[rowIdx][m] < target) {
                l = m + 1;
            } else if (matrix[rowIdx][m] > target) {
                r = m - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
