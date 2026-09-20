class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length - k + 1; i++) {
            int windowMax = nums[i];

            for (int j = i; j < i + k; j++) {
                windowMax = Math.max(windowMax, nums[j]);
            }

            res[i] = windowMax;
        }
        
        return res;
    }
}
