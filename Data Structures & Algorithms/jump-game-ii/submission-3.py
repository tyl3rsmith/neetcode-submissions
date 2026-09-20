class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0 # tells us our bfs window

        while r < len(nums) - 1:
            # find the farthest we can jump
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # update window and inc reset
            l = r + 1
            r = farthest
            res += 1
        return res

        