class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            maxElem = nums[i]
            for j in range(i, i + k):
                maxElem = max(maxElem, nums[j])
            res.append(maxElem)

        return res