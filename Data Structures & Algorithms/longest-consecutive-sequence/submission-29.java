class Solution {
    public int longestConsecutive(int[] nums) {
        // hash set for removal of duplicates and O(1) lookups
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longest = 0;
        for (int num : numSet) {
            // check if we can start a streak
            if (!numSet.contains(num - 1)) {
                int currLength = 1;
                while (numSet.contains(++num)) {
                    currLength++;
                }
                
                longest = Math.max(longest, currLength);
            }
        }
        
        return longest;
    }   
}
