class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            # find the farthest jump values in our window can make
            farthest = 0
            for i in range(l, r + 1): 
                farthest = max(farthest, i + nums[i])
            
            # update window
            l = r + 1
            r = farthest
            res += 1
        
        return res