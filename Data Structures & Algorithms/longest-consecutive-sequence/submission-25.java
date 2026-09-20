class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int longest = 1, curr = 1;

        for (int i = 1; i < nums.length; i++) {
            // skip duplicates
            if (nums[i] == nums[i - 1]) {
                continue;
            }

            // part of streak
            if (nums[i] == nums[i - 1] + 1) {
                curr++;
            } else { // not part of streak try a new sequence
                curr = 1;
            }

            longest = Math.max(longest, curr);
        }
        return longest;
    }   
}
