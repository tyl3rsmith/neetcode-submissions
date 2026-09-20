class Solution {
    public int findDuplicate(int[] nums) {
        // guaranteed a duplicate since every int its between [1, n]
        // and the length is n + 1
        boolean[] seen = new boolean[nums.length];

        for (int num : nums) {
            if (seen[num]) {
                return num;
            }
            seen[num] = true;
        }
        return -1;
    }
}
