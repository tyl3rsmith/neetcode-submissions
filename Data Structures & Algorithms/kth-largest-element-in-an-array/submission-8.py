class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
            nums[p], nums[r] = pivot, nums[p]

            if p > target_index:
                return quickSelect(l, p - 1)
            elif p < target_index:
                return quickSelect(p + 1, r)
            else:
                return pivot
        
        return quickSelect(0, len(nums) - 1)

