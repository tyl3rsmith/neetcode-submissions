class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(i, j): # i: right, j: down
            # we made it to the base case
            if i == m - 1 and j == n - 1:
                return 1
            
            # we over shot this path is invalid
            if i > m - 1 or j > n - 1:
                return 0

            # option 1 move right
            a = dfs(i + 1, j)

            # option 2 move down
            b = dfs(i, j + 1)

            return a + b
        
        return dfs(0, 0)