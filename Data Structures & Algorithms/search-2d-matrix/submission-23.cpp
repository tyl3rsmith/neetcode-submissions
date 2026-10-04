class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size();
        int COLS = matrix[0].size();

        int top = 0, bottom = ROWS - 1;

        while (top <= bottom) {
            int row = top + (bottom - top) / 2;

            if (target >= matrix[row][0] && target <= matrix[row][COLS - 1]) {
                break;
            } else if (target > matrix[row][COLS - 1]) {
                top = row + 1;
            } else {
                bottom = row - 1;
            }
        }

        if (!(top <= bottom)) {
            return false;
        }

        int row = top + (bottom - top) / 2;
        
        int left = 0, right = COLS - 1;
        while (left <= right) {
            int col = left + (right - left) / 2;

            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                left = col + 1;
            } else {
                right = col - 1;
            }
        }

        return false;
    }
};
