class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row, end_row = 0, len(matrix) - 1

        while start_row <= end_row:
            mid = start_row + ((end_row - start_row) // 2)
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l, r = 0, len(matrix[mid])

                while l <= r:
                    m = l + ((r - l) // 2)
                    if matrix[mid][m] < target:
                        l = m + 1
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        return True
                
                return False

            elif target > matrix[mid][-1]: # check the larger vals
                start_row = mid + 1
            elif target < matrix[mid][0]: # check the smaller vals
                end_row = mid - 1
        
        return False
        