class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # binary search for the row
        l, r = 0, rows - 1
        row = -1

        while l <= r:
            m = l + (r - l) // 2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                row = m
                break

            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        # binary search the cols in the row that we found it should be in
        l, r = 0, cols - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False

