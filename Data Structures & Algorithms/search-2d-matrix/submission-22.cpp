class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size();
        int COLS = matrix[0].size();

        int l = 0;
        int r = COLS - 1;

        for (int row = 0; row < ROWS; row++) {
            if (target >= matrix[row][l] && target <= matrix[row][r]) {
                if (target == matrix[row][l] || target == matrix[row][r]) {
                    return true;
                }
                
                while (l < r) {
                    int m = l + (r - l) / 2;

                    if (matrix[row][m] == target) {
                        return true;
                    } else if (matrix[row][m] < target) {
                        l++;
                    } else {
                        r--;
                    }
                }

            }
        }

        return false;
    }
};
