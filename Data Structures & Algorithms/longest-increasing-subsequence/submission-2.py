class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums) + 1) for _ in range(len(nums))]
        def dfs(i, j):
            # i: current index we're considering (rows)
            # j: index of the previous element included (cols)
            # extend cols by 1 since j can be -1 so we map to j + 1 so it starts at 0

            # base case: no more numbers to consider LIS is len 0
            if i == len(nums):
                return 0
            
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]
            
            # we dont include i, j stays the same
            LIS = dfs(i + 1, j)
            
            # we include i if its valid
            # valid if there's no prev num: j == -1 or
            # the prev num is smaller than the curr num
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include

            memo[i][j + 1] = LIS
            return LIS

        res = dfs(0, -1)
        print(memo)
        return res


        [[4, -1, -1, -1, -1, -1, -1, -1],
         [4, 0, -1, -1, -1, -1, -1, -1],
         [3, 0, 3, -1, -1, -1, -1, -1], 
         [3, 0, 3, 1, -1, -1, -1, -1], 
         [2, 0, 2, 1, 2, -1, -1, -1], 
         [2, 0, 2, 1, 2, 1, -1, -1], 
         [1, 0, 1, 1, 1, 1, 1, -1]]

    