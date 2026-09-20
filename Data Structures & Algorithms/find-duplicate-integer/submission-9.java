class Solution {
    public int findDuplicate(int[] nums) {
        for (int num : nums) {
            int index = Math.abs(num); // abs val cause future nay be negative
            if (nums[index] < 0) {
                return Math.abs(num);
            } 
            nums[index] *= -1;
        }
        return -1;
    }
}
