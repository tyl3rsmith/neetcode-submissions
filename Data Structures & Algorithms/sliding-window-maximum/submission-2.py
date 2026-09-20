class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            windowMax = nums[i]
            for j in range(i, i + k):
                windowMax = max(windowMax, nums[j])

            res.append(windowMax)

        return res
                
        