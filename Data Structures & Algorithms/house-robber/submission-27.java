class Solution {
    public int rob(int[] nums) {
        // [rob1, rob2, 1, 1, 3, 3]
        int rob1 = 0, rob2 = 0;

        for (int n : nums) {
            int temp = rob2;
            rob2 = Math.max(n + rob1, rob2);
            rob1 = temp;
        }

        return rob2;

    }
}
