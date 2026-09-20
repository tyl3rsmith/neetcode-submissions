class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for the row
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            
            elif target > matrix[row][-1]:
                top = row + 1
            
            else:
                break
        
        if top > bottom:
            return False

        row = top + (bottom - top) // 2

        # binary search the column
        l, r = 0, len(matrix[row])
        while l <= r:
            m = l + (r - l) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False
        


                    