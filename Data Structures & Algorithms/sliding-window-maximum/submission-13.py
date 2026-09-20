class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque() # monotonically decreasing
        l = r = 0

        while r < len(nums):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)

            # remove out of bound maxes
            if l > d[0]:
                d.popleft()

            # now we can start adding results
            if (r + 1) >= k:
                res.append(nums[d[0]])
                l += 1 # move to next window

            r += 1
        
        return res
