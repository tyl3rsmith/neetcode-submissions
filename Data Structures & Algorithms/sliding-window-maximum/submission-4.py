class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = deque() # indices

        while r < len(nums):
            # pop smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # if left value is out of bounds remove the left value from the window
            if l > q[0]:
                q.popleft()
            
            # edge case: window needs to be at least size k to update output
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
        
            r += 1

        return res
                
        