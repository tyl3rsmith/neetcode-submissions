class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row: 0 -> 2
        # col: 0 -> 3

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == target:
                    return True
        return False
        