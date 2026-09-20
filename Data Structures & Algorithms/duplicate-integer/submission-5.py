class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given int arr nums
        return true if any value appears more than once in the array
        """
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
        return False
         