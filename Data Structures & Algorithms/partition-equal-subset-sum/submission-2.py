class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, target = len(nums), sum(nums) // 2

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        for i in range(n - 1, -1, -1):
            nextDP = set()
            for val in dp:
                if (val + nums[i]) == target:
                    return True
                nextDP.add(val)
                nextDP.add(val + nums[i])
            dp = nextDP

        return False

        {0, 4, 3, 7, 2, 6, 5}

