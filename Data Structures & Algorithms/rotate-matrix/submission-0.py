class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        for r in range(len(matrix) // 2):
            matrix[r], matrix[len(matrix) - r - 1] = matrix[len(matrix) - r - 1], matrix[r]
            
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]