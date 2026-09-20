class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalPost = n - 1

        for i in range(n - 2, -1, -1):
            jumpDist = i + nums[i]

            if goalPost in range(jumpDist + 1):
                goalPost = i
        
        return goalPost == 0