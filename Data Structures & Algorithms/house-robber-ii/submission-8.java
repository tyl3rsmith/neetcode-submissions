class Solution {
    public int robber(int[] nums) {
        int rob1 = 0, rob2 = 0;

        for (int n : nums) {
            int temp = rob2;
            rob2 = Math.max(n + rob1, rob2);
            rob1 = temp;
        }

        return rob2;
    }

    public int rob(int[] nums) {
        int temp = Math.max(nums[0], robber(Arrays.copyOfRange(nums, 1, nums.length)));

        return Math.max(temp, robber(Arrays.copyOfRange(nums, 0, nums.length - 1)));
    }
}
