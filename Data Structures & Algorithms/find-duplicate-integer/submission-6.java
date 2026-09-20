class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] seen = new boolean[nums.length];

        for (int num : nums) {
            if (seen[num - 1]) {
                return num;
            }
            seen[num - 1] = true;
        }
        return -1;
    }
}
