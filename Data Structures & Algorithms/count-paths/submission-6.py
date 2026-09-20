class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # compute unique paths row by 1
        # last row only has 1 path to the base case
        row = [1] * n

        for i in range(m - 1):
            # above the old row
            newRow = [1] * n
            for j in range(n - 2, -1, -1): # skip last most col bc its gonna be 1
                newRow[j] = newRow[j + 1] + row[j] # look right and below
            row = newRow

        return row[0]