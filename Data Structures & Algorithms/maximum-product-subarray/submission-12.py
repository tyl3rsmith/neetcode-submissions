class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # max_dp[i] = maximum product of a subarray ending at i
        max_dp = [0] * n

        # min_dp[i] = minimum product of a subarray ending at i
        min_dp = [0] * n

        # Base case
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, n):
            x = nums[i]

            # We can either:
            # 1. Start a new subarray with x
            # 2. Multiply x by the previous maximum
            # 3. Multiply x by the previous minimum
            #
            # We need both max and min because:
            # negative × negative = positive
            max_dp[i] = max(
                x,
                x * max_dp[i - 1],
                x * min_dp[i - 1]
            )

            min_dp[i] = min(
                x,
                x * max_dp[i - 1],
                x * min_dp[i - 1]
            )

        # The answer can end at any index
        return max(max_dp)