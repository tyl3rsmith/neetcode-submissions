class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [0] * (len(nums1) + len(nums2))

        n1, n2, i = 0, 0, 0
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                nums[i] = nums1[n1]
                n1 += 1
                i += 1
            else:
                nums[i] = nums2[n2]
                n2 += 1
                i += 1
        
        while n1 < len(nums1):
            nums[i] = nums1[n1]
            n1 += 1
            i += 1
        
        while n2 < len(nums2):
            nums[i] = nums2[n2]
            n2 += 1
            i += 1


        if len(nums) % 2 == 1:
            return float(nums[(len(nums) - 1) // 2])
        else:
            return float((nums[(len(nums) - 1) // 2] + nums[((len(nums) - 1) // 2) + 1]) / 2)
        
        
        