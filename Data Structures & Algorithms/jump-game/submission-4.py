class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n - 2, -1, -1):
            jumpDist = min(i + nums[i], n - 1) # edge case, cant jump past end val

            # try every jump
            for j in range(i + 1, jumpDist + 1):
                if dp[j]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]
