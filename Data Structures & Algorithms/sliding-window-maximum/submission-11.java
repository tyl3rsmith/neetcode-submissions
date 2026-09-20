class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] res = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length - k + 1; i++) {
            int maxElem = nums[i];

            for (int j = i; j < i + k; j++) {
                maxElem = Math.max(maxElem, nums[j]);
            }

            res[i] = maxElem;
        }
        return res;
    }
}
