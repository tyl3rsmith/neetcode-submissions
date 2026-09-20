class Solution {
    public int robHouse(int i, int[] nums, int[] memo) {
        if (i >= nums.length) {
            return 0;
        }

        if (memo[i] != -1) {
            return memo[i];
        }
        memo[i] = Math.max(nums[i] + robHouse(i + 2, nums, memo), robHouse(i + 1, nums, memo));
        return memo[i];
    }

    public int rob(int[] nums) {
        int[] memo = new int[nums.length];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }

        return robHouse(0, nums, memo);
    }
}
