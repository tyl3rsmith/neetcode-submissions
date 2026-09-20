class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        
        l = 0
        for r in range(k, len(nums) + 1):
            maxHeap = []
            for i in range(l, r):
                maxHeap.append(-nums[i])
            heapq.heapify(maxHeap)
            res.append(-maxHeap[0])

            l += 1
        
        return res
