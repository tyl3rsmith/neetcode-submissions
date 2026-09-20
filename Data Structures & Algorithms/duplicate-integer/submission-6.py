class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given int arr nums
        return true if any value appears more than once in the array
        """
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        
        return False
         