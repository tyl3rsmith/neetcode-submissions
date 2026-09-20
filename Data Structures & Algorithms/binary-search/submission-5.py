class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        

        l = 0
        r = len(nums) - 1
        m = (r // 2) + 1

        print(l)
        print(m)
        print(r)

        while l <= r:
            if target == nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
                m = (l + r) // 2
            elif nums[m] > target:
                r = m - 1
                m = (l + r) // 2
        return -1
        
        