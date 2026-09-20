class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row, end_row = 0, len(matrix) - 1
        while start_row <= end_row:
            mid_row = start_row + ((end_row - start_row) // 2)

            if target > matrix[mid_row][-1]:
                start_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                end_row = mid_row - 1
            else:
                break
        
        if not (start_row <= end_row):
            return False
        
        row = start_row + ((end_row - start_row) // 2)
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
